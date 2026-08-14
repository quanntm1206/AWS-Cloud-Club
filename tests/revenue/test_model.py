from dataclasses import replace
from pathlib import Path
from shutil import copyfile

import joblib
import pandas as pd
import pytest

from ml_roadmap.revenue.model import (
    candidate_models,
    chronological_split,
    load_bundle,
    predict_revenue,
    train_all,
    train_country,
)


def _frame(days: int = 60) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for offset, date in enumerate(pd.date_range("2024-01-01", periods=days)):
        rows.extend(
            [
                {
                    "date": date,
                    "country": "france",
                    "revenue": 90 + offset * 1.5 + (offset % 7) * 3,
                },
                {
                    "date": date,
                    "country": "viet_nam",
                    "revenue": 120 + offset * 2 + (offset % 7) * 2,
                },
            ]
        )
    return pd.DataFrame(rows)


def test_candidate_models_include_baseline_and_two_real_models() -> None:
    assert list(candidate_models()) == ["baseline_mean", "ridge", "random_forest"]


def test_chronological_split_holds_out_latest_rows() -> None:
    features = pd.DataFrame({"value": range(20)})
    target = pd.Series(range(20))

    train_x, test_x, train_y, test_y = chronological_split(features, target, test_fraction=0.2)

    assert train_x["value"].tolist() == list(range(16))
    assert test_x["value"].tolist() == list(range(16, 20))
    assert train_y.tolist() == list(range(16))
    assert test_y.tolist() == list(range(16, 20))


def test_train_country_compares_models_and_persists_bundle(tmp_path: Path) -> None:
    result = train_country(_frame(), "france", tmp_path, tag="test")

    assert set(result.model_rmse) == {"baseline_mean", "ridge", "random_forest"}
    assert result.rmse <= result.baseline_rmse
    assert result.artifact_path.parent == tmp_path
    assert result.artifact_path.is_file()

    bundle = load_bundle(tmp_path, "france", tag="test")
    assert bundle.country == "france"
    assert bundle.model_name == result.best_model
    assert len(bundle.history) == 60
    assert bundle.feature_names == (
        "day_of_week",
        "month",
        "trend",
        "lag_1",
        "lag_7",
        "rolling_mean_7",
    )
    assert bundle.metrics["rmse"] == result.rmse
    assert bundle.metrics["baseline_rmse"] == result.baseline_rmse


def test_load_bundle_rejects_incompatible_feature_schema(tmp_path: Path) -> None:
    result = train_country(_frame(), "france", tmp_path, tag="test")
    bundle = load_bundle(tmp_path, "france", tag="test")
    joblib.dump(replace(bundle, feature_names=("unknown",)), result.artifact_path)

    with pytest.raises(ValueError, match="feature schema"):
        load_bundle(tmp_path, "france", tag="test")


def test_load_bundle_rejects_wrong_country_and_invalid_invariants(tmp_path: Path) -> None:
    train_all(_frame(), tmp_path, tag="test")
    france_path = tmp_path / "model-france-test.joblib"
    copyfile(tmp_path / "model-viet_nam-test.joblib", france_path)
    with pytest.raises(ValueError, match="country identity"):
        load_bundle(tmp_path, "france", tag="test")

    train_country(_frame(), "france", tmp_path, tag="test")
    bundle = load_bundle(tmp_path, "france", tag="test")
    invalid_bundles = [
        (replace(bundle, model_version="unsupported"), "model version"),
        (replace(bundle, history=()), "history"),
        (
            replace(bundle, metrics={"rmse": float("nan"), "baseline_rmse": 1.0}),
            "metrics",
        ),
    ]
    for invalid, match in invalid_bundles:
        joblib.dump(invalid, france_path)
        with pytest.raises(ValueError, match=match):
            load_bundle(tmp_path, "france", tag="test")


def test_train_all_builds_country_and_combined_models(tmp_path: Path) -> None:
    results = train_all(_frame(), tmp_path, tag="test")

    assert [result.country for result in results] == ["all", "france", "viet_nam"]
    assert (tmp_path / "metrics-test.json").is_file()
    assert {path.name for path in tmp_path.glob("model-*-test.joblib")} == {
        "model-all-test.joblib",
        "model-france-test.joblib",
        "model-viet_nam-test.joblib",
    }


def test_prediction_is_deterministic_and_non_negative(tmp_path: Path) -> None:
    train_country(_frame(), "all", tmp_path, tag="test")
    bundle = load_bundle(tmp_path, "all", tag="test")

    first = predict_revenue(bundle, "2024-03-15")
    second = predict_revenue(bundle, "2024-03-15")

    assert first == second
    assert first >= 0

    with pytest.raises(ValueError, match="after the latest observation"):
        predict_revenue(bundle, "2024-02-01")


def test_load_bundle_rejects_missing_country(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError, match="no trained model"):
        load_bundle(tmp_path, "missing", tag="test")
