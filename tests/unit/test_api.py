from fastapi.testclient import TestClient

from ml_roadmap.api import create_app
from ml_roadmap.artifacts import ModelBundle
from ml_roadmap.config import TrainConfig
from ml_roadmap.data import make_demo_churn_data
from ml_roadmap.train_tabular import train


def _client_with_model() -> TestClient:
    result = train(TrainConfig(target="churn", seed=42), make_demo_churn_data(rows=120, seed=42))
    bundle = ModelBundle(result.pipeline, result.feature_names, result.threshold)
    return TestClient(create_app(bundle))


def test_health_and_unavailable_contract() -> None:
    client = TestClient(create_app(bundle=None))
    assert client.get("/health").json() == {"status": "degraded", "model_loaded": False}
    response = client.post("/predict", json={})
    assert response.status_code == 503
    assert response.json() == {"detail": "model unavailable"}


def test_valid_and_invalid_payload_contract() -> None:
    client = _client_with_model()
    valid = {"age": 35, "tenure_months": 12, "monthly_charge": 79, "region": "north", "contract": "monthly"}
    response = client.post("/predict", json=valid)
    assert response.status_code == 200
    assert set(response.json()) == {"label", "probability", "threshold"}

    missing = client.post("/predict", json={key: value for key, value in valid.items() if key != "age"})
    assert missing.status_code == 422
    assert "missing fields" in missing.json()["detail"]

    wrong_type = client.post("/predict", json={**valid, "age": "bad"})
    assert wrong_type.status_code == 422
    assert wrong_type.json() == {"detail": "field types or values do not satisfy the model schema"}


def test_uvicorn_factory_starts_without_artifact_environment(monkeypatch) -> None:  # type: ignore[no-untyped-def]
    monkeypatch.delenv("ML_ROADMAP_ARTIFACT_DIR", raising=False)
    app = create_app()
    assert app.title == "ML Roadmap Tabular Inference"
