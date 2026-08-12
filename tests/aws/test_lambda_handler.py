import hashlib
import importlib.util
import json
import sys
import types
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.modules.setdefault("boto3", types.SimpleNamespace(client=lambda service: None))
SPEC = importlib.util.spec_from_file_location("aws_lambda_handler", ROOT / "aws/lambda/handler.py")
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)

MODEL = {
    "numeric": ["age", "tenure_months", "monthly_charge"],
    "categorical": ["region", "contract"],
    "numeric_imputer": [35.0, 18.0, 70.0],
    "numeric_mean": [35.0, 18.0, 70.0],
    "numeric_scale": [10.0, 10.0, 20.0],
    "categorical_imputer": ["north", "monthly"],
    "categories": [["north", "south"], ["annual", "monthly"]],
    "coefficients": [0.1, -0.2, 0.4, -0.1, 0.2, -0.3, 0.5],
    "intercept": -0.1,
    "threshold": 0.5,
}


def _envelope(model: dict[str, object]) -> dict[str, object]:
    encoded = json.dumps(model, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return {"schema_version": 1, "model_sha256": hashlib.sha256(encoded).hexdigest(), "model": model}


def test_lambda_accepts_valid_contract_without_logging_payload() -> None:
    event = json.loads((ROOT / "aws/events/valid.json").read_text(encoding="utf-8"))
    MODULE._MODEL = MODEL
    response = MODULE.lambda_handler(event, None)
    assert response["statusCode"] == 200


def test_lambda_rejects_missing_fields() -> None:
    event = json.loads((ROOT / "aws/events/invalid.json").read_text(encoding="utf-8"))
    response = MODULE.lambda_handler(event, None)
    assert response["statusCode"] == 422
    assert "monthly_charge" in response["body"]


def test_lambda_scores_portable_model_without_sklearn() -> None:
    model = {
        "numeric": ["age"],
        "categorical": ["region"],
        "numeric_imputer": [30.0],
        "numeric_mean": [30.0],
        "numeric_scale": [10.0],
        "categorical_imputer": ["north"],
        "categories": [["north", "south"]],
        "coefficients": [0.5, -0.2, 0.4],
        "intercept": -0.1,
        "threshold": 0.5,
    }
    probability = MODULE.score({"age": 40, "region": "south"}, model)
    assert 0.0 < probability < 1.0


def test_lambda_maps_bad_field_to_422() -> None:
    event = json.loads((ROOT / "aws/events/valid.json").read_text(encoding="utf-8"))
    event["age"] = "bad"
    MODULE._MODEL = MODEL
    response = MODULE.lambda_handler(event, None)
    assert response == {"statusCode": 422, "body": '{"error": "invalid field type or value"}'}


def test_lambda_maps_model_load_failure_to_503(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    event = json.loads((ROOT / "aws/events/valid.json").read_text(encoding="utf-8"))
    MODULE._MODEL = None

    def fail() -> dict[str, object]:
        raise OSError("offline")

    monkeypatch.setattr(MODULE, "load_model", fail)
    response = MODULE.lambda_handler(event, None)
    assert response == {"statusCode": 503, "body": '{"error": "model unavailable"}'}


def test_lambda_rejects_tampered_portable_envelope(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    event = json.loads((ROOT / "aws/events/valid.json").read_text(encoding="utf-8"))
    envelope = _envelope(MODEL)
    envelope["model_sha256"] = "0" * 64
    body = types.SimpleNamespace(read=lambda: json.dumps(envelope).encode())
    client = types.SimpleNamespace(get_object=lambda **kwargs: {"Body": body})
    monkeypatch.setattr(MODULE.boto3, "client", lambda service: client)
    MODULE._MODEL = None
    response = MODULE.lambda_handler(event, None)
    assert response == {"statusCode": 503, "body": '{"error": "model unavailable"}'}


def test_lambda_rejects_nonfinite_client_value() -> None:
    event = json.loads((ROOT / "aws/events/valid.json").read_text(encoding="utf-8"))
    event["age"] = "1e999"
    MODULE._MODEL = MODEL
    response = MODULE.lambda_handler(event, None)
    assert response["statusCode"] == 422
