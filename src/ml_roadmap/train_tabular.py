from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

from .config import TrainConfig, load_config
from .data import split_features_target
from .evaluate import binary_metrics
from .features import build_preprocessor


@dataclass
class TrainResult:
    pipeline: Pipeline
    metrics: dict[str, float | int]
    feature_names: tuple[str, ...]
    config: TrainConfig
    threshold: float


def _select_threshold(truth: pd.Series, probability: np.ndarray) -> float:
    from sklearn.metrics import f1_score

    candidates = [value / 100 for value in range(20, 81, 5)]
    scored = [(float(f1_score(truth, probability >= value, zero_division=0)), value) for value in candidates]
    return max(scored, key=lambda pair: (pair[0], -abs(pair[1] - 0.5)))[1]


def train(config: TrainConfig, frame: pd.DataFrame) -> TrainResult:
    features, target = split_features_target(frame, config.target)
    numeric = features.select_dtypes(include="number").columns.tolist()
    categorical = [column for column in features.columns if column not in numeric]
    development_x, test_x, development_y, test_y = train_test_split(
        features,
        target,
        test_size=config.test_size,
        random_state=config.seed,
        stratify=target,
    )
    relative_validation_size = config.validation_size / (1 - config.test_size)
    train_x, validation_x, train_y, validation_y = train_test_split(
        development_x,
        development_y,
        test_size=relative_validation_size,
        random_state=config.seed,
        stratify=development_y,
    )
    pipeline = Pipeline(
        [
            ("preprocess", build_preprocessor(numeric, categorical)),
            ("model", LogisticRegression(max_iter=500, random_state=config.seed)),
        ]
    )
    pipeline.fit(train_x, train_y)
    validation_probability = pipeline.predict_proba(validation_x)[:, 1]
    threshold = (
        _select_threshold(validation_y, validation_probability)
        if config.tune_threshold
        else config.threshold
    )
    probability = pipeline.predict_proba(test_x)[:, 1]
    dummy = DummyClassifier(strategy="prior").fit(train_x, train_y)
    dummy_probability = dummy.predict_proba(test_x)[:, 1]
    metrics: dict[str, float | int] = binary_metrics(
        test_y.to_numpy(), probability, threshold
    )
    validation_metrics = binary_metrics(validation_y.to_numpy(), validation_probability, threshold)
    metrics.update({f"validation_{name}": value for name, value in validation_metrics.items()})
    metrics["selected_threshold"] = threshold
    metrics["dummy_roc_auc"] = float(
        binary_metrics(test_y.to_numpy(), dummy_probability, config.threshold)["roc_auc"]
    )
    metrics["test_rows"] = len(test_x)
    return TrainResult(
        pipeline=pipeline,
        metrics=metrics,
        feature_names=tuple(features.columns),
        config=config,
        threshold=threshold,
    )


def main() -> int:
    import argparse

    from .artifacts import save_artifact

    parser = argparse.ArgumentParser(description="Train the tabular demo pipeline")
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    result = train(load_config(args.config), pd.read_csv(args.data))
    manifest = save_artifact(result, args.output)
    print({"metrics": result.metrics, "sha256": manifest.sha256})
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
