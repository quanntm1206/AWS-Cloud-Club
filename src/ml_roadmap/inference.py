from __future__ import annotations

from dataclasses import dataclass

import pandas as pd

from .artifacts import ModelBundle


class PayloadError(ValueError):
    pass


@dataclass(frozen=True)
class PredictionResponse:
    label: int
    probability: float
    threshold: float


def predict(payload: dict[str, object], bundle: ModelBundle) -> PredictionResponse:
    missing = sorted(set(bundle.feature_names) - set(payload))
    if missing:
        raise PayloadError(f"missing fields: {missing}")
    frame = pd.DataFrame([{name: payload[name] for name in bundle.feature_names}])
    try:
        probability = float(bundle.pipeline.predict_proba(frame)[0, 1])
    except (TypeError, ValueError) as exc:
        raise PayloadError("field types or values do not satisfy the model schema") from exc
    return PredictionResponse(
        label=int(probability >= bundle.threshold),
        probability=probability,
        threshold=bundle.threshold,
    )
