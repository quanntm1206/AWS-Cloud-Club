import json
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from ml_roadmap.artifacts import load_bundle, load_portable_model, save_artifact, score_portable
from ml_roadmap.config import TrainConfig, load_config
from ml_roadmap.data import make_demo_churn_data, split_features_target
from ml_roadmap.inference import PayloadError, predict
from ml_roadmap.train_tabular import train
from ml_roadmap.validation import DataSchema, validate_frame


def test_numpy_vectorization_oracle() -> None:
    features = np.array([[1.0, 2.0], [3.0, 4.0]])
    weights = np.array([0.5, -0.25])
    assert (features @ weights).tolist() == [0.0, 0.5]


def test_finite_difference_gradient_matches_analytic() -> None:
    features = np.array([[1.0], [2.0], [3.0]])
    target = np.array([2.0, 4.0, 6.0])
    weight = np.array([1.5])
    analytic = (2 / len(features)) * features.T @ (features @ weight - target)
    epsilon = 1e-6
    loss = lambda w: np.mean((features @ w - target) ** 2)  # noqa: E731
    numeric = (loss(weight + epsilon) - loss(weight - epsilon)) / (2 * epsilon)
    assert analytic.item() == pytest.approx(numeric, abs=1e-6)


def test_load_config_rejects_unknown_keys(tmp_path: Path) -> None:
    path = tmp_path / "config.yml"
    path.write_text("target: churn\nunknown: true\n", encoding="utf-8")
    with pytest.raises(ValueError, match="unknown config keys"):
        load_config(path)


def test_validation_reports_missing_and_extra_columns() -> None:
    frame = pd.DataFrame({"age": [20], "debug": [1]})
    report = validate_frame(frame, DataSchema(required=("age", "income"), allow_extra=False))
    assert report.missing == ("income",)
    assert report.extra == ("debug",)
    assert not report.valid


def test_training_is_deterministic_and_artifact_reloads(tmp_path: Path) -> None:
    frame = make_demo_churn_data(rows=120, seed=7)
    config = TrainConfig(target="churn", seed=17, test_size=0.25)
    first = train(config, frame)
    second = train(config, frame)
    assert first.metrics == second.metrics
    manifest = save_artifact(first, tmp_path)
    assert len(manifest.sha256) == 64
    bundle = load_bundle(tmp_path)
    features, _ = split_features_target(frame, "churn")
    assert bundle.pipeline.predict(features.head(5)).tolist() == first.pipeline.predict(
        features.head(5)
    ).tolist()
    portable = load_portable_model(tmp_path / "portable_model.json")
    sample = features.iloc[0].to_dict()
    expected_probability = float(first.pipeline.predict_proba(features.iloc[[0]])[0, 1])
    assert score_portable(sample, portable) == pytest.approx(expected_probability, abs=1e-9)

    envelope = json.loads((tmp_path / "portable_model.json").read_text(encoding="utf-8"))
    envelope["model"]["intercept"] += 1
    (tmp_path / "portable_model.json").write_text(json.dumps(envelope), encoding="utf-8")
    with pytest.raises(ValueError, match="checksum mismatch"):
        load_portable_model(tmp_path / "portable_model.json")


def test_inference_handles_unknown_category_and_rejects_missing_column(tmp_path: Path) -> None:
    frame = make_demo_churn_data(rows=100, seed=3)
    result = train(TrainConfig(target="churn", seed=2), frame)
    save_artifact(result, tmp_path)
    bundle = load_bundle(tmp_path)
    sample = frame.drop(columns="churn").iloc[0].to_dict()
    sample["region"] = "unknown-region"
    response = predict(sample, bundle)
    assert 0.0 <= response.probability <= 1.0
    sample.pop("age")
    with pytest.raises(PayloadError, match="missing fields"):
        predict(sample, bundle)
