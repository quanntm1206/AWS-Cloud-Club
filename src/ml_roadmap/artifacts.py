from __future__ import annotations

import hashlib
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Any, TypedDict, cast

import joblib
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from .train_tabular import TrainResult


@dataclass(frozen=True)
class ArtifactManifest:
    model_file: str
    sha256: str
    feature_names: tuple[str, ...]
    threshold: float


@dataclass(frozen=True)
class ModelBundle:
    pipeline: Any
    feature_names: tuple[str, ...]
    threshold: float


class PortableModel(TypedDict):
    numeric: list[str]
    categorical: list[str]
    numeric_imputer: list[float]
    numeric_mean: list[float]
    numeric_scale: list[float]
    categorical_imputer: list[str]
    categories: list[list[str]]
    coefficients: list[float]
    intercept: float
    threshold: float


class PortableEnvelope(TypedDict):
    schema_version: int
    model_sha256: str
    model: PortableModel


def _canonical_model_bytes(model: PortableModel) -> bytes:
    return json.dumps(model, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def _portable_envelope(model: PortableModel) -> PortableEnvelope:
    return {
        "schema_version": 1,
        "model_sha256": hashlib.sha256(_canonical_model_bytes(model)).hexdigest(),
        "model": model,
    }


def _portable_logistic_model(result: TrainResult) -> PortableModel:
    preprocess = result.pipeline.named_steps["preprocess"]
    model = result.pipeline.named_steps["model"]
    if not isinstance(preprocess, ColumnTransformer) or not isinstance(model, LogisticRegression):
        raise TypeError("portable export only supports the roadmap logistic pipeline")
    numeric_pipeline = preprocess.named_transformers_["numeric"]
    categorical_pipeline = preprocess.named_transformers_["categorical"]
    if not isinstance(numeric_pipeline, Pipeline) or not isinstance(categorical_pipeline, Pipeline):
        raise TypeError("unexpected preprocessing pipeline")
    numeric_columns = list(preprocess.transformers_[0][2])
    categorical_columns = list(preprocess.transformers_[1][2])
    numeric_imputer = numeric_pipeline.named_steps["imputer"]
    scaler = numeric_pipeline.named_steps["scale"]
    categorical_imputer = categorical_pipeline.named_steps["imputer"]
    encoder = categorical_pipeline.named_steps["onehot"]
    if not isinstance(numeric_imputer, SimpleImputer) or not isinstance(scaler, StandardScaler):
        raise TypeError("unexpected numeric pipeline")
    if not isinstance(categorical_imputer, SimpleImputer) or not isinstance(encoder, OneHotEncoder):
        raise TypeError("unexpected categorical pipeline")
    return {
        "numeric": numeric_columns,
        "categorical": categorical_columns,
        "numeric_imputer": [float(value) for value in numeric_imputer.statistics_],
        "numeric_mean": [float(value) for value in scaler.mean_],
        "numeric_scale": [float(value) for value in scaler.scale_],
        "categorical_imputer": [str(value) for value in categorical_imputer.statistics_],
        "categories": [[str(value) for value in values] for values in encoder.categories_],
        "coefficients": [float(value) for value in model.coef_[0]],
        "intercept": float(model.intercept_[0]),
        "threshold": result.threshold,
    }


def save_artifact(result: TrainResult, output_dir: Path) -> ArtifactManifest:
    output_dir.mkdir(parents=True, exist_ok=True)
    model_path = output_dir / "model.joblib"
    joblib.dump(result.pipeline, model_path)
    sha256 = hashlib.sha256(model_path.read_bytes()).hexdigest()
    manifest = ArtifactManifest(
        model_file=model_path.name,
        sha256=sha256,
        feature_names=result.feature_names,
        threshold=result.threshold,
    )
    (output_dir / "manifest.json").write_text(
        json.dumps(asdict(manifest), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    (output_dir / "metrics.json").write_text(
        json.dumps(result.metrics, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    portable_model = _portable_logistic_model(result)
    (output_dir / "portable_model.json").write_text(
        json.dumps(_portable_envelope(portable_model), ensure_ascii=False, indent=2), encoding="utf-8"
    )
    return manifest


def load_bundle(output_dir: Path) -> ModelBundle:
    data = json.loads((output_dir / "manifest.json").read_text(encoding="utf-8"))
    model_path = output_dir / data["model_file"]
    actual = hashlib.sha256(model_path.read_bytes()).hexdigest()
    if actual != data["sha256"]:
        raise ValueError("artifact checksum mismatch")
    return ModelBundle(
        pipeline=joblib.load(model_path),
        feature_names=tuple(data["feature_names"]),
        threshold=float(data["threshold"]),
    )


def load_portable_model(path: Path) -> PortableModel:
    envelope = cast(dict[str, object], json.loads(path.read_text(encoding="utf-8")))
    if envelope.get("schema_version") != 1 or not isinstance(envelope.get("model"), dict):
        raise ValueError("unsupported portable artifact schema")
    model = cast(PortableModel, envelope["model"])
    expected = envelope.get("model_sha256")
    actual = hashlib.sha256(_canonical_model_bytes(model)).hexdigest()
    if not isinstance(expected, str) or expected != actual:
        raise ValueError("portable artifact checksum mismatch")
    return model


def score_portable(payload: dict[str, object], model: PortableModel) -> float:
    values: list[float] = []
    numeric = list(model["numeric"])
    for index, name in enumerate(numeric):
        raw = payload.get(str(name))
        if raw is None:
            numeric_value = model["numeric_imputer"][index]
        elif isinstance(raw, (int, float, str)):
            numeric_value = float(raw)
        else:
            raise ValueError(f"numeric field has invalid type: {name}")
        values.append(
            (numeric_value - float(model["numeric_mean"][index]))
            / float(model["numeric_scale"][index])
        )
    categorical = list(model["categorical"])
    for index, name in enumerate(categorical):
        raw = payload.get(str(name))
        categorical_value = model["categorical_imputer"][index] if raw is None else str(raw)
        values.extend(
            1.0 if categorical_value == category else 0.0
            for category in model["categories"][index]
        )
    logit = float(model["intercept"]) + sum(
        coefficient * value
        for coefficient, value in zip(model["coefficients"], values, strict=True)
    )
    return 1.0 / (1.0 + math.exp(-logit))
