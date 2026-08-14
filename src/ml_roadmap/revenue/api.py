from __future__ import annotations

import os
from collections.abc import Awaitable, Callable
from datetime import date
from pathlib import Path
from threading import Lock
from time import perf_counter

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, ConfigDict, Field
from starlette.responses import Response

from .data import load_revenue_csv, normalize_country
from .model import load_bundle, predict_revenue
from .observability import log_prediction, read_events, summarize_performance


class PredictionRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")

    country: str = Field(default="all", min_length=1)
    date: date


def create_app(
    *,
    data_path: Path | None = None,
    model_dir: Path | None = None,
    log_dir: Path | None = None,
    tag: str | None = None,
) -> FastAPI:
    resolved_data = data_path or Path(
        os.getenv("REVENUE_DATA_PATH", "capstones/country-revenue/data/revenue.csv")
    )
    resolved_models = model_dir or Path(
        os.getenv("REVENUE_MODEL_DIR", "capstones/country-revenue/models")
    )
    resolved_logs = log_dir or Path(
        os.getenv("REVENUE_LOG_DIR", "capstones/country-revenue/logs")
    )
    resolved_tag: str = tag or os.getenv("REVENUE_TAG") or "prod"
    app = FastAPI(title="Country Revenue Forecasting API", version="1.0.0")
    telemetry_lock = Lock()
    telemetry_write_failures = 0

    def record_prediction(
        *,
        country: str,
        target_date: str,
        prediction: float | None,
        model_name: str | None,
        model_version: str | None,
        runtime_ms: float,
        status: str,
    ) -> None:
        nonlocal telemetry_write_failures
        try:
            log_prediction(
                resolved_logs,
                country=country,
                target_date=target_date,
                prediction=prediction,
                model_name=model_name,
                model_version=model_version,
                runtime_ms=runtime_ms,
                status=status,
                tag=resolved_tag,
            )
        except OSError:
            with telemetry_lock:
                telemetry_write_failures += 1

    @app.middleware("http")
    async def capture_request_start(
        request: Request, call_next: Callable[[Request], Awaitable[Response]]
    ) -> Response:
        request.state.started_at = perf_counter()
        return await call_next(request)

    def model_coverage() -> tuple[bool, dict[str, object]]:
        try:
            frame = load_revenue_csv(resolved_data)
            expected = ["all", *sorted(frame["country"].unique().tolist())]
            data_ready = True
        except (FileNotFoundError, ValueError):
            expected = []
            data_ready = False
        missing: list[str] = []
        for country in expected:
            try:
                load_bundle(resolved_models, country, tag=resolved_tag)
            except (FileNotFoundError, ValueError):
                missing.append(country)
        return data_ready, {
            "expected_models": len(expected),
            "available_models": len(expected) - len(missing),
            "missing_models": missing,
        }

    @app.exception_handler(RequestValidationError)
    async def request_validation_error(
        request: Request, exc: RequestValidationError
    ) -> JSONResponse:
        if request.url.path == "/predict":
            started_at = float(getattr(request.state, "started_at", perf_counter()))
            record_prediction(
                country="invalid",
                target_date="invalid",
                prediction=None,
                model_name=None,
                model_version=None,
                runtime_ms=(perf_counter() - started_at) * 1000,
                status="error",
            )
        return JSONResponse(status_code=422, content={"detail": jsonable_encoder(exc.errors())})

    @app.get("/health")
    def health() -> dict[str, object]:
        data_ready, coverage = model_coverage()
        models_ready = bool(coverage["expected_models"]) and not coverage["missing_models"]
        return {
            "status": "ready" if data_ready and models_ready else "degraded",
            "data_ready": data_ready,
            "models_ready": models_ready,
            **coverage,
        }

    @app.post("/predict")
    def predict(payload: PredictionRequest) -> dict[str, object]:
        started = perf_counter()
        try:
            country = normalize_country(payload.country)
        except ValueError as exc:
            record_prediction(
                country="invalid",
                target_date=payload.date.isoformat(),
                prediction=None,
                model_name=None,
                model_version=None,
                runtime_ms=(perf_counter() - started) * 1000,
                status="error",
            )
            raise HTTPException(status_code=422, detail=str(exc)) from exc
        target_date = payload.date.isoformat()
        try:
            bundle = load_bundle(resolved_models, country, tag=resolved_tag)
        except FileNotFoundError as exc:
            runtime_ms = (perf_counter() - started) * 1000
            record_prediction(
                country=country,
                target_date=target_date,
                prediction=None,
                model_name=None,
                model_version=None,
                runtime_ms=runtime_ms,
                status="error",
            )
            raise HTTPException(status_code=404, detail=str(exc)) from exc
        try:
            prediction = predict_revenue(bundle, target_date)
        except ValueError as exc:
            runtime_ms = (perf_counter() - started) * 1000
            record_prediction(
                country=country,
                target_date=target_date,
                prediction=None,
                model_name=bundle.model_name,
                model_version=bundle.model_version,
                runtime_ms=runtime_ms,
                status="error",
            )
            raise HTTPException(status_code=422, detail=str(exc)) from exc

        runtime_ms = (perf_counter() - started) * 1000
        record_prediction(
            country=country,
            target_date=target_date,
            prediction=prediction,
            model_name=bundle.model_name,
            model_version=bundle.model_version,
            runtime_ms=runtime_ms,
            status="success",
        )
        return {
            "status": "success",
            "country": country,
            "target_date": target_date,
            "predicted_revenue": round(prediction, 2),
            "model_used": bundle.model_name,
            "model_version": bundle.model_version,
            "runtime_ms": round(runtime_ms, 3),
        }

    @app.get("/metrics")
    def metrics() -> dict[str, object]:
        summary = summarize_performance(resolved_logs, tag=resolved_tag)
        _, coverage = model_coverage()
        summary["model_coverage"] = coverage
        with telemetry_lock:
            summary["telemetry_write_failures"] = telemetry_write_failures
        return summary

    @app.get("/logs/{kind}")
    def logs(kind: str, limit: int = Query(default=100, ge=1, le=1_000)) -> dict[str, object]:
        if kind not in {"train", "predict"}:
            raise HTTPException(status_code=400, detail="kind must be 'train' or 'predict'")
        return {
            "kind": kind,
            "tag": resolved_tag,
            "events": read_events(resolved_logs, kind, tag=resolved_tag, limit=limit),
        }

    return app
