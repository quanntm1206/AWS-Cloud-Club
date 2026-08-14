from __future__ import annotations

import json
import re
from collections import deque
from datetime import UTC, datetime
from pathlib import Path
from threading import RLock
from typing import Any

import numpy as np

LOG_KINDS = {"train", "predict"}
MAX_LOG_BYTES = 2_000_000
LOG_LOCK = RLock()


def _safe_token(value: str) -> str:
    token = re.sub(r"[^a-z0-9_-]+", "_", value.strip().lower()).strip("_")
    if not token:
        raise ValueError("log tag must contain a letter or number")
    return token


def _log_path(log_dir: Path, kind: str, tag: str) -> Path:
    if kind not in LOG_KINDS:
        raise ValueError(f"log kind must be one of {sorted(LOG_KINDS)}")
    return log_dir / f"{kind}-{_safe_token(tag)}.jsonl"


def _append_event(log_dir: Path, kind: str, payload: dict[str, Any], tag: str) -> None:
    log_dir.mkdir(parents=True, exist_ok=True)
    event = {
        "timestamp": datetime.now(UTC).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
        **payload,
    }
    path = _log_path(log_dir, kind, tag)
    with LOG_LOCK:
        if path.is_file() and path.stat().st_size >= MAX_LOG_BYTES:
            rotated = path.with_suffix(path.suffix + ".1")
            rotated.unlink(missing_ok=True)
            path.replace(rotated)
        with path.open("a", encoding="utf-8", newline="\n") as stream:
            stream.write(json.dumps(event, sort_keys=True, separators=(",", ":")) + "\n")


def log_training(
    log_dir: Path,
    *,
    country: str,
    model_name: str,
    model_version: str,
    rmse: float,
    baseline_rmse: float,
    runtime_ms: float,
    run_id: str,
    tag: str = "prod",
) -> None:
    _append_event(
        log_dir,
        "train",
        {
            "country": country,
            "model_name": model_name,
            "model_version": model_version,
            "rmse": rmse,
            "baseline_rmse": baseline_rmse,
            "runtime_ms": runtime_ms,
            "run_id": run_id,
        },
        tag,
    )


def log_prediction(
    log_dir: Path,
    *,
    country: str,
    target_date: str,
    prediction: float | None,
    model_name: str | None,
    model_version: str | None,
    runtime_ms: float,
    status: str,
    tag: str = "prod",
) -> None:
    _append_event(
        log_dir,
        "predict",
        {
            "country": country,
            "target_date": target_date,
            "prediction": prediction,
            "model_name": model_name,
            "model_version": model_version,
            "runtime_ms": runtime_ms,
            "status": status,
        },
        tag,
    )


def read_events(
    log_dir: Path,
    kind: str,
    *,
    tag: str = "prod",
    limit: int = 1_000,
) -> list[dict[str, Any]]:
    if not 1 <= limit <= 10_000:
        raise ValueError("limit must be between 1 and 10000")
    path = _log_path(log_dir, kind, tag)
    if not path.is_file():
        return []
    events: deque[dict[str, Any]] = deque(maxlen=limit)
    with LOG_LOCK:
        lines = path.read_text(encoding="utf-8").splitlines()
    for number, line in enumerate(lines, start=1):
        try:
            event = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL in {path} at line {number}") from exc
        if not isinstance(event, dict):
            raise ValueError(f"invalid log event in {path} at line {number}")
        events.append(event)
    return list(events)


def summarize_performance(log_dir: Path, *, tag: str = "prod") -> dict[str, Any]:
    events = read_events(log_dir, "predict", tag=tag, limit=10_000)
    training_events = read_events(log_dir, "train", tag=tag, limit=10_000)
    if events:
        latencies = [float(event["runtime_ms"]) for event in events]
        error_count = sum(event.get("status") != "success" for event in events)
        versions = sorted(
            {str(event["model_version"]) for event in events if event.get("model_version")}
        )
        summary: dict[str, Any] = {
            "request_count": len(events),
            "error_count": error_count,
            "error_rate": error_count / len(events),
            "average_latency_ms": float(np.mean(latencies)),
            "p95_latency_ms": float(np.percentile(latencies, 95)),
            "countries": sorted({str(event["country"]) for event in events}),
            "model_versions": versions,
        }
    else:
        summary = {
            "request_count": 0,
            "error_count": 0,
            "error_rate": 0.0,
            "average_latency_ms": 0.0,
            "p95_latency_ms": 0.0,
            "countries": [],
            "model_versions": [],
        }

    latest_metrics: dict[str, dict[str, object]] = {}
    for event in training_events:
        latest_metrics[str(event["country"])] = {
            "model_name": event["model_name"],
            "model_version": event["model_version"],
            "rmse": event["rmse"],
            "baseline_rmse": event["baseline_rmse"],
        }
    run_ids = {str(event.get("run_id", event["timestamp"])) for event in training_events}
    summary["training_run_count"] = len(run_ids)
    summary["training_event_count"] = len(training_events)
    summary["latest_model_metrics"] = latest_metrics
    summary["window"] = {
        "scope": "active_log",
        "max_events": 10_000,
        "rotation_bytes": MAX_LOG_BYTES,
    }
    return summary
