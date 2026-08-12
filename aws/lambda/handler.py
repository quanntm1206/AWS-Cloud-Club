from __future__ import annotations

import hashlib
import json
import math
import os
from typing import Any

import boto3

REQUIRED = {"age", "tenure_months", "monthly_charge", "region", "contract"}
_MODEL: dict[str, Any] | None = None


def score(payload: dict[str, Any], model: dict[str, Any]) -> float:
    values: list[float] = []
    for index, name in enumerate(model["numeric"]):
        raw = payload.get(name)
        value = float(model["numeric_imputer"][index]) if raw is None else float(raw)
        if not math.isfinite(value):
            raise ValueError(f"non-finite numeric field: {name}")
        values.append((value - model["numeric_mean"][index]) / model["numeric_scale"][index])
    for index, name in enumerate(model["categorical"]):
        raw = payload.get(name)
        value = model["categorical_imputer"][index] if raw is None else str(raw)
        values.extend(1.0 if value == category else 0.0 for category in model["categories"][index])
    logit = model["intercept"] + sum(
        coefficient * value
        for coefficient, value in zip(model["coefficients"], values, strict=True)
    )
    return 1.0 / (1.0 + math.exp(-logit))


def load_model() -> dict[str, Any]:
    global _MODEL
    if _MODEL is None:
        response = boto3.client("s3").get_object(
            Bucket=os.environ["ARTIFACT_BUCKET"],
            Key=os.environ.get("ARTIFACT_KEY", "models/portable_model.json"),
        )
        envelope = json.loads(response["Body"].read().decode("utf-8"))
        if envelope.get("schema_version") != 1 or not isinstance(envelope.get("model"), dict):
            raise ValueError("unsupported portable artifact schema")
        model_bytes = json.dumps(
            envelope["model"], ensure_ascii=False, sort_keys=True, separators=(",", ":")
        ).encode("utf-8")
        if envelope.get("model_sha256") != hashlib.sha256(model_bytes).hexdigest():
            raise ValueError("portable artifact checksum mismatch")
        _MODEL = envelope["model"]
    return _MODEL


def lambda_handler(event: dict[str, Any], context: Any) -> dict[str, Any]:
    del context
    body = event.get("body", event)
    if isinstance(body, str):
        try:
            body = json.loads(body)
        except json.JSONDecodeError:
            return {"statusCode": 400, "body": json.dumps({"error": "invalid JSON"})}
    if not isinstance(body, dict):
        return {"statusCode": 422, "body": json.dumps({"error": "body must be an object"})}
    missing = sorted(REQUIRED - set(body))
    if missing:
        return {
            "statusCode": 422,
            "body": json.dumps({"error": "missing fields", "fields": missing}),
        }
    try:
        model = load_model()
    except Exception:  # Service boundary: SDK, network, JSON, schema and artifact failures map to 503.
        return {"statusCode": 503, "body": json.dumps({"error": "model unavailable"})}
    try:
        probability = score(body, model)
    except (OverflowError, ValueError, TypeError):
        return {"statusCode": 422, "body": json.dumps({"error": "invalid field type or value"})}
    try:
        threshold = float(model.get("threshold", 0.5))
        if not math.isfinite(threshold) or not 0 <= threshold <= 1:
            raise ValueError("invalid threshold")
    except (ValueError, TypeError):
        return {"statusCode": 503, "body": json.dumps({"error": "model unavailable"})}
    return {
        "statusCode": 200,
        "body": json.dumps(
            {"label": int(probability >= threshold), "probability": probability, "threshold": threshold}
        ),
    }
