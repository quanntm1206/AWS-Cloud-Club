from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

import ml_roadmap.revenue.observability as observability
from ml_roadmap.revenue.observability import (
    log_prediction,
    log_training,
    read_events,
    summarize_performance,
)


def test_training_logs_are_isolated_by_directory_and_tag(tmp_path: Path) -> None:
    test_logs = tmp_path / "isolated-test-logs"

    log_training(
        test_logs,
        country="all",
        model_name="ridge",
        model_version="1.0.0",
        rmse=3.2,
        baseline_rmse=9.5,
        runtime_ms=12.0,
        run_id="run-1",
        tag="test",
    )

    assert (test_logs / "train-test.jsonl").is_file()
    assert not (test_logs / "train-prod.jsonl").exists()
    event = read_events(test_logs, "train", tag="test")[0]
    assert event["country"] == "all"
    assert event["rmse"] == 3.2
    assert event["timestamp"].endswith("Z")


def test_prediction_logs_power_performance_monitoring(tmp_path: Path) -> None:
    log_prediction(
        tmp_path,
        country="france",
        target_date="2024-03-01",
        prediction=123.4,
        model_name="ridge",
        model_version="1.0.0",
        runtime_ms=10.0,
        status="success",
        tag="test",
    )
    log_prediction(
        tmp_path,
        country="all",
        target_date="2024-03-01",
        prediction=None,
        model_name=None,
        model_version=None,
        runtime_ms=30.0,
        status="error",
        tag="test",
    )

    summary = summarize_performance(tmp_path, tag="test")

    assert summary == {
        "request_count": 2,
        "error_count": 1,
        "error_rate": 0.5,
        "average_latency_ms": 20.0,
        "p95_latency_ms": 29.0,
        "countries": ["all", "france"],
        "model_versions": ["1.0.0"],
        "training_run_count": 0,
        "training_event_count": 0,
        "latest_model_metrics": {},
        "window": {
            "scope": "active_log",
            "max_events": 10_000,
            "rotation_bytes": observability.MAX_LOG_BYTES,
        },
    }


def test_empty_monitoring_summary_is_well_defined(tmp_path: Path) -> None:
    assert summarize_performance(tmp_path, tag="test") == {
        "request_count": 0,
        "error_count": 0,
        "error_rate": 0.0,
        "average_latency_ms": 0.0,
        "p95_latency_ms": 0.0,
        "countries": [],
        "model_versions": [],
        "training_run_count": 0,
        "training_event_count": 0,
        "latest_model_metrics": {},
        "window": {
            "scope": "active_log",
            "max_events": 10_000,
            "rotation_bytes": observability.MAX_LOG_BYTES,
        },
    }


def test_monitoring_includes_latest_model_quality_against_baseline(tmp_path: Path) -> None:
    log_training(
        tmp_path,
        country="france",
        model_name="ridge",
        model_version="1.0.0",
        rmse=4.5,
        baseline_rmse=10.0,
        runtime_ms=15.0,
        run_id="run-1",
        tag="test",
    )

    summary = summarize_performance(tmp_path, tag="test")

    assert summary["training_run_count"] == 1
    assert summary["training_event_count"] == 1
    assert summary["latest_model_metrics"] == {
        "france": {
            "model_name": "ridge",
            "model_version": "1.0.0",
            "rmse": 4.5,
            "baseline_rmse": 10.0,
        }
    }


def test_training_run_count_deduplicates_country_events(tmp_path: Path) -> None:
    for country in ("all", "france"):
        log_training(
            tmp_path,
            country=country,
            model_name="ridge",
            model_version="1.0.0",
            rmse=4.5,
            baseline_rmse=10.0,
            runtime_ms=15.0,
            run_id="same-run",
            tag="test",
        )

    summary = summarize_performance(tmp_path, tag="test")

    assert summary["training_run_count"] == 1
    assert summary["training_event_count"] == 2


def test_read_events_returns_only_requested_recent_window(tmp_path: Path) -> None:
    for day in range(5):
        log_prediction(
            tmp_path,
            country="france",
            target_date=f"2024-03-{day + 1:02d}",
            prediction=float(day),
            model_name="ridge",
            model_version="1.0.0",
            runtime_ms=1.0,
            status="success",
            tag="test",
        )

    events = read_events(tmp_path, "predict", tag="test", limit=2)

    assert [event["prediction"] for event in events] == [3.0, 4.0]
    with pytest.raises(ValueError, match="limit"):
        read_events(tmp_path, "predict", tag="test", limit=0)


def test_log_rotation_bounds_active_file_size(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(observability, "MAX_LOG_BYTES", 1)
    for day in range(2):
        log_prediction(
            tmp_path,
            country="france",
            target_date=f"2024-03-{day + 1:02d}",
            prediction=float(day),
            model_name="ridge",
            model_version="1.0.0",
            runtime_ms=1.0,
            status="success",
            tag="test",
        )

    assert (tmp_path / "predict-test.jsonl.1").is_file()
    assert [event["prediction"] for event in read_events(tmp_path, "predict", tag="test")] == [
        1.0
    ]


def test_concurrent_rotation_does_not_fail_writers(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.setattr(observability, "MAX_LOG_BYTES", 500)

    def write_event(index: int) -> None:
        log_prediction(
            tmp_path,
            country="france",
            target_date=f"2024-04-{index % 28 + 1:02d}",
            prediction=float(index),
            model_name="ridge",
            model_version="1.0.0",
            runtime_ms=1.0,
            status="success",
            tag="test",
        )

    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = [executor.submit(write_event, index) for index in range(100)]
    assert all(future.exception() is None for future in futures)


def test_read_events_rejects_unknown_log_kind(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="log kind"):
        read_events(tmp_path, "secrets", tag="test")
