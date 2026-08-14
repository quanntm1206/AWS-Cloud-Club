from __future__ import annotations

import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any, cast

import joblib
import numpy as np
import pandas as pd
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error

from .data import (
    FEATURE_COLUMNS,
    aggregate_daily,
    build_forecast_features,
    engineer_features,
    normalize_country,
    validate_revenue_frame,
)

MODEL_VERSION = "1.0.0"


@dataclass(frozen=True)
class ModelBundle:
    country: str
    model_name: str
    model_version: str
    model: Any
    history: tuple[tuple[str, float], ...]
    feature_names: tuple[str, ...]
    metrics: dict[str, float]


@dataclass(frozen=True)
class TrainingResult:
    country: str
    best_model: str
    rmse: float
    baseline_rmse: float
    model_rmse: dict[str, float]
    artifact_path: Path
    test_rows: int


def candidate_models() -> dict[str, Any]:
    return {
        "baseline_mean": DummyRegressor(strategy="mean"),
        "ridge": Ridge(alpha=1.0),
        "random_forest": RandomForestRegressor(
            n_estimators=60,
            max_depth=8,
            min_samples_leaf=2,
            random_state=42,
            n_jobs=1,
        ),
    }


def chronological_split(
    features: pd.DataFrame,
    target: pd.Series,
    test_fraction: float = 0.2,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    if not 0 < test_fraction < 1:
        raise ValueError("test_fraction must be between 0 and 1")
    if len(features) != len(target) or len(features) < 5:
        raise ValueError("features and target must have the same length of at least 5")
    test_rows = max(1, int(len(features) * test_fraction))
    split = len(features) - test_rows
    return (
        features.iloc[:split],
        features.iloc[split:],
        target.iloc[:split],
        target.iloc[split:],
    )


def _safe_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9_-]+", "_", value.strip().lower()).strip("_")
    if not token:
        raise ValueError("artifact tag must contain a letter or number")
    return token


def _artifact_path(model_dir: Path, country: str, tag: str) -> Path:
    return model_dir / f"model-{_safe_token(country)}-{_safe_token(tag)}.joblib"


def train_country(
    frame: pd.DataFrame,
    country: str | None,
    model_dir: Path,
    *,
    tag: str = "prod",
) -> TrainingResult:
    label = "all" if country is None else normalize_country(country)
    daily = aggregate_daily(frame, label)
    features, target, _ = engineer_features(daily)
    train_x, test_x, train_y, test_y = chronological_split(features, target)

    fitted: dict[str, Any] = {}
    scores: dict[str, float] = {}
    for name, estimator in candidate_models().items():
        estimator.fit(train_x, train_y)
        prediction = estimator.predict(test_x)
        scores[name] = float(np.sqrt(mean_squared_error(test_y, prediction)))
        fitted[name] = estimator

    best_name = min(scores, key=scores.__getitem__)
    model_dir.mkdir(parents=True, exist_ok=True)
    artifact_path = _artifact_path(model_dir, label, tag)
    history = tuple(
        (pd.Timestamp(row.date).date().isoformat(), float(row.revenue))
        for row in daily.itertuples(index=False)
    )
    bundle = ModelBundle(
        country=label,
        model_name=best_name,
        model_version=MODEL_VERSION,
        model=fitted[best_name],
        history=history,
        feature_names=FEATURE_COLUMNS,
        metrics={
            "rmse": scores[best_name],
            "baseline_rmse": scores["baseline_mean"],
        },
    )
    joblib.dump(bundle, artifact_path)
    return TrainingResult(
        country=label,
        best_model=best_name,
        rmse=scores[best_name],
        baseline_rmse=scores["baseline_mean"],
        model_rmse=scores,
        artifact_path=artifact_path,
        test_rows=len(test_x),
    )


def train_all(
    frame: pd.DataFrame,
    model_dir: Path,
    *,
    tag: str = "prod",
) -> list[TrainingResult]:
    clean = validate_revenue_frame(frame)
    labels = ["all", *sorted(clean["country"].unique().tolist())]
    results = [train_country(clean, label, model_dir, tag=tag) for label in labels]
    metrics_path = model_dir / f"metrics-{_safe_token(tag)}.json"
    payload = [
        {
            "country": result.country,
            "best_model": result.best_model,
            "rmse": result.rmse,
            "baseline_rmse": result.baseline_rmse,
            "model_rmse": result.model_rmse,
            "test_rows": result.test_rows,
        }
        for result in results
    ]
    metrics_path.write_text(json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8")
    return results


def load_bundle(model_dir: Path, country: str | None, *, tag: str = "prod") -> ModelBundle:
    label = "all" if country is None else normalize_country(country)
    path = _artifact_path(model_dir, label, tag)
    if not path.is_file():
        raise FileNotFoundError(f"no trained model for country={label!r}, tag={tag!r}")
    bundle = cast(object, joblib.load(path))
    if not isinstance(bundle, ModelBundle):
        raise ValueError(f"invalid model bundle: {path}")
    if bundle.country != label:
        raise ValueError(
            f"model country identity {bundle.country!r} does not match requested {label!r}"
        )
    if bundle.model_version != MODEL_VERSION:
        raise ValueError(f"unsupported model version: {bundle.model_version!r}")
    if bundle.feature_names != FEATURE_COLUMNS:
        raise ValueError(
            f"model feature schema {bundle.feature_names!r} does not match {FEATURE_COLUMNS!r}"
        )
    if len(bundle.history) < 7:
        raise ValueError("model history must contain at least 7 observations")
    history = pd.DataFrame(bundle.history, columns=["date", "revenue"])
    history["date"] = pd.to_datetime(history["date"], errors="coerce")
    revenue = pd.to_numeric(history["revenue"], errors="coerce")
    if (
        history["date"].isna().any()
        or not history["date"].is_monotonic_increasing
        or history["date"].duplicated().any()
        or revenue.isna().any()
        or not np.isfinite(revenue).all()
        or (revenue < 0).any()
    ):
        raise ValueError("model history is invalid")
    required_metrics = {"rmse", "baseline_rmse"}
    if set(bundle.metrics) != required_metrics or any(
        not math.isfinite(value) or value < 0 for value in bundle.metrics.values()
    ):
        raise ValueError("model metrics are invalid")
    if bundle.metrics["rmse"] > bundle.metrics["baseline_rmse"]:
        raise ValueError("model metrics do not beat or match the baseline")
    if not callable(getattr(bundle.model, "predict", None)):
        raise ValueError("model bundle does not contain a predictor")
    return bundle


def predict_revenue(bundle: ModelBundle, target_date: str | pd.Timestamp) -> float:
    try:
        date = pd.Timestamp(target_date)
    except (TypeError, ValueError) as exc:
        raise ValueError("target_date must be a valid date") from exc
    latest_observation = pd.Timestamp(bundle.history[-1][0])
    if date.normalize() <= latest_observation:
        raise ValueError(
            f"target_date must be after the latest observation ({latest_observation.date()})"
        )
    daily = pd.DataFrame(bundle.history, columns=["date", "revenue"])
    features = build_forecast_features(daily, date)
    prediction = float(bundle.model.predict(features)[0])
    return max(0.0, prediction)
