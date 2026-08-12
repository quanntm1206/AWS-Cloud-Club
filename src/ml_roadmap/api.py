from __future__ import annotations

import os
from dataclasses import asdict
from pathlib import Path

from fastapi import FastAPI, HTTPException

from .artifacts import ModelBundle, load_bundle
from .inference import PayloadError, predict


def create_app(bundle: ModelBundle | None = None) -> FastAPI:
    artifact_dir = os.getenv("ML_ROADMAP_ARTIFACT_DIR")
    if bundle is None and artifact_dir:
        bundle = load_bundle(Path(artifact_dir))
    app = FastAPI(title="ML Roadmap Tabular Inference")

    @app.get("/health")
    def health() -> dict[str, object]:
        loaded = bundle is not None
        return {"status": "ok" if loaded else "degraded", "model_loaded": loaded}

    @app.post("/predict")
    def predict_route(payload: dict[str, object]) -> dict[str, object]:
        if bundle is None:
            raise HTTPException(status_code=503, detail="model unavailable")
        try:
            return asdict(predict(payload, bundle))
        except PayloadError as exc:
            raise HTTPException(status_code=422, detail=str(exc)) from exc

    return app
