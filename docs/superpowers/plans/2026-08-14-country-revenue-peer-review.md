# Country Revenue Peer-Review Implementation Plan

## File Map

- `src/ml_roadmap/revenue/data.py`: schema validation, CSV ingestion, daily
  aggregation, lag/calendar feature construction.
- `src/ml_roadmap/revenue/model.py`: chronological split, candidate comparison,
  per-country/all training, artifact load and prediction.
- `src/ml_roadmap/revenue/observability.py`: isolated JSONL logs and performance
  summaries.
- `src/ml_roadmap/revenue/api.py`: FastAPI contracts and dependency-injected app.
- `src/ml_roadmap/revenue/generate_data.py`: deterministic automation fixture.
- `src/ml_roadmap/revenue/eda.py`: EDA and baseline comparison plots.
- `tests/revenue/`: unit and API tests grouped by rubric concern.
- `capstones/country-revenue/`: runnable data, models, plots, and evidence README.

## Task 1: Contracts And Ingestion

1. Add failing tests for required CSV columns, normalized countries, aggregate
   time series, deterministic lag features, and malformed data.
2. Run `python -m pytest tests/revenue/test_data.py -q`; expect missing-module
   failure.
3. Implement the smallest typed ingestion and feature functions.
4. Re-run the focused tests; expect pass.

## Task 2: Model Comparison And Artifacts

1. Add failing tests for chronological split, three candidates, baseline
   metrics, country/all artifacts, deterministic prediction, and unknown model.
2. Run `python -m pytest tests/revenue/test_model.py -q`; expect failure.
3. Implement training, comparison, artifact persistence, and prediction.
4. Re-run data and model tests; expect pass.

## Task 3: Logging And Monitoring

1. Add failing tests proving test logs stay under `tmp_path`, JSONL records are
   complete, and metric summaries calculate counts/errors/latency.
2. Run `python -m pytest tests/revenue/test_observability.py -q`; expect failure.
3. Implement append/read/summarize functions.
4. Re-run focused tests; expect pass.

## Task 4: API

1. Add failing tests for health, country prediction, `all`, validation errors,
   missing models, metrics, and log retrieval.
2. Run `python -m pytest tests/revenue/test_api.py -q`; expect failure.
3. Implement the app factory using explicit data/model/log roots.
4. Re-run all revenue tests; expect pass.

## Task 5: Data, EDA, And Review Evidence

1. Add tests for deterministic generated data and four required PNG outputs.
2. Implement generator and headless plotting script.
3. Add `matplotlib` to project and lock dependencies.
4. Generate capstone CSV, models, metrics, and plots.
5. Write the rubric evidence README with exact commands and endpoints.

## Task 6: Docker, CI, And Full Verification

1. Update Docker to generate data, train models, render plots, run tests, and
   serve the revenue API.
2. Add CI Docker build and container health/prediction smoke checks.
3. Run `make check`.
4. Run `docker build` and smoke `/health`, country `/predict`, and `all`.
5. Inspect generated plots, clean status, and complete rubric traceability.
