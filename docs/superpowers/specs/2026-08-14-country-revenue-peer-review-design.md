# Country Revenue Peer-Review Capstone Design

## Goal

Add a self-contained country revenue forecasting capstone that satisfies the
12 peer-review checks without changing the existing churn and CV teaching
paths.

## Architecture

The new `ml_roadmap.revenue` package owns ingestion, feature engineering,
training, artifacts, observability, prediction, EDA, and the FastAPI app. Every
read/write boundary accepts an explicit path. Production uses paths configured
by environment variables; tests use `tmp_path` and never touch repository
models or logs.

Training builds one aggregate `all` model and one model per country. It uses a
chronological holdout and compares a mean baseline, Ridge, and Random Forest by
RMSE. The selected fitted model, feature schema, history-derived forecast
context, metrics, and version are saved together.

The API exposes `/health`, `/predict`, `/metrics`, and `/logs/{kind}`. A request
contains a target date and either a country name or `all`. Prediction logs record
runtime, status, model version, country, target date, and prediction. The
metrics endpoint aggregates request count, errors, latency, and model coverage.

## Automation And Evidence

- `python -m ml_roadmap.revenue.generate_data` creates deterministic demo CSV.
- `python -m ml_roadmap.revenue.train` trains all country and aggregate models.
- `python -m ml_roadmap.revenue.eda` writes EDA and baseline-comparison PNGs.
- `make test` remains the single full-suite command.
- Docker builds a ready-to-serve image with generated data, trained models,
  plots, and passing tests.
- CI runs tests, lint, typecheck, Docker build, and a container smoke check.
- `capstones/country-revenue/README.md` maps every rubric question to evidence.

## Safety

Synthetic data keeps the project runnable and license-safe. A real CSV can be
mounted or supplied through the same documented schema. Runtime directories
are configurable; no test code writes production artifacts.
