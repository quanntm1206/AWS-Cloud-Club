from pathlib import Path

import pandas as pd
import pytest
from fastapi.testclient import TestClient

import ml_roadmap.revenue.api as revenue_api
from ml_roadmap.revenue.api import create_app
from ml_roadmap.revenue.model import train_all


def _write_data(path: Path, days: int = 60) -> pd.DataFrame:
    rows: list[dict[str, object]] = []
    for offset, date in enumerate(pd.date_range("2024-01-01", periods=days)):
        for country, base in (("france", 100), ("viet_nam", 140)):
            rows.append(
                {
                    "date": date,
                    "country": country,
                    "revenue": base + offset * 1.5 + (offset % 7) * 4,
                }
            )
    frame = pd.DataFrame(rows)
    frame.to_csv(path, index=False)
    return frame


def test_health_reports_model_readiness(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    _write_data(data_path)
    client = TestClient(
        create_app(data_path=data_path, model_dir=tmp_path / "models", log_dir=tmp_path / "logs")
    )

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "degraded",
        "data_ready": True,
        "models_ready": False,
        "expected_models": 3,
        "available_models": 0,
        "missing_models": ["all", "france", "viet_nam"],
    }

    train_all(_write_data(data_path), tmp_path / "models", tag="prod")
    ready = client.get("/health")
    assert ready.json()["status"] == "ready"
    assert ready.json()["missing_models"] == []

    (tmp_path / "models" / "model-france-prod.joblib").unlink()
    partial = client.get("/health")
    assert partial.json()["status"] == "degraded"
    assert partial.json()["missing_models"] == ["france"]


def test_predict_supports_specific_country_and_all(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    frame = _write_data(data_path)
    model_dir = tmp_path / "models"
    log_dir = tmp_path / "logs"
    train_all(frame, model_dir, tag="test")
    client = TestClient(
        create_app(data_path=data_path, model_dir=model_dir, log_dir=log_dir, tag="test")
    )

    france = client.post("/predict", json={"country": "france", "date": "2024-03-15"})
    combined = client.post("/predict", json={"country": "all", "date": "2024-03-15"})

    assert france.status_code == 200
    assert france.json()["country"] == "france"
    assert france.json()["predicted_revenue"] >= 0
    assert combined.status_code == 200
    assert combined.json()["country"] == "all"
    assert combined.json()["predicted_revenue"] >= france.json()["predicted_revenue"]
    assert (log_dir / "predict-test.jsonl").is_file()
    assert not (log_dir / "predict-prod.jsonl").exists()


def test_predict_validates_payload_and_unknown_country(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    frame = _write_data(data_path)
    model_dir = tmp_path / "models"
    train_all(frame, model_dir, tag="test")
    client = TestClient(
        create_app(
            data_path=data_path,
            model_dir=model_dir,
            log_dir=tmp_path / "logs",
            tag="test",
        )
    )

    invalid = client.post("/predict", json={"country": "france", "date": "bad"})
    invalid_country = client.post("/predict", json={"country": "---", "date": "2024-03-15"})
    past_date = client.post("/predict", json={"country": "france", "date": "2024-02-01"})
    unknown = client.post("/predict", json={"country": "missing", "date": "2024-03-15"})

    assert invalid.status_code == 422
    assert invalid_country.status_code == 422
    assert past_date.status_code == 422
    assert unknown.status_code == 404
    assert "no trained model" in unknown.json()["detail"]
    metrics = client.get("/metrics").json()
    assert metrics["request_count"] == 4
    assert metrics["error_count"] == 4
    events = client.get("/logs/predict").json()["events"]
    assert events[0]["runtime_ms"] > 0


def test_metrics_and_logs_expose_observability(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    frame = _write_data(data_path)
    model_dir = tmp_path / "models"
    log_dir = tmp_path / "logs"
    train_all(frame, model_dir, tag="test")
    client = TestClient(
        create_app(data_path=data_path, model_dir=model_dir, log_dir=log_dir, tag="test")
    )
    client.post("/predict", json={"country": "france", "date": "2024-03-15"})
    client.post("/predict", json={"country": "missing", "date": "2024-03-15"})

    metrics = client.get("/metrics")
    logs = client.get("/logs/predict")
    limited_logs = client.get("/logs/predict?limit=1")
    invalid_kind = client.get("/logs/private")

    assert metrics.status_code == 200
    assert metrics.json()["request_count"] == 2
    assert metrics.json()["error_count"] == 1
    assert metrics.json()["model_coverage"] == {
        "expected_models": 3,
        "available_models": 3,
        "missing_models": [],
    }
    assert len(logs.json()["events"]) == 2
    assert len(limited_logs.json()["events"]) == 1
    assert invalid_kind.status_code == 400


def test_logging_failure_does_not_break_prediction(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    data_path = tmp_path / "revenue.csv"
    frame = _write_data(data_path)
    model_dir = tmp_path / "models"
    train_all(frame, model_dir, tag="test")

    def fail_logging(*args: object, **kwargs: object) -> None:
        raise OSError("disk unavailable")

    monkeypatch.setattr(revenue_api, "log_prediction", fail_logging)
    client = TestClient(
        create_app(
            data_path=data_path,
            model_dir=model_dir,
            log_dir=tmp_path / "logs",
            tag="test",
        )
    )

    response = client.post("/predict", json={"country": "france", "date": "2024-03-15"})

    assert response.status_code == 200
    assert client.get("/metrics").json()["telemetry_write_failures"] == 1
