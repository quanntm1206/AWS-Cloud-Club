# Country Revenue Forecasting Capstone

This self-contained capstone predicts revenue for one country or all countries
combined. It includes deterministic demo data so reviewers can run the complete
system without credentials. Replace the CSV with real data using the same
`date,country,revenue` schema when available.

Prediction dates must be later than the newest observation in the training CSV;
requests for historical dates are rejected to prevent look-ahead leakage.

## Run Locally

```bash
python -m pip install -r requirements.lock
python -m pip install -e . --no-deps
make revenue-build
python scripts/run-unit-tests.py
make revenue-serve
```

Windows without `make` can run the three commands from the `revenue-build`
target directly. All generated files stay under this capstone directory.

## API Examples

Specific country:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"country":"france","date":"2018-09-15"}'
```

All countries combined:

```bash
curl -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"country":"all","date":"2018-09-15"}'
```

Operational endpoints:

- `GET /health`: data readiness and complete per-country/aggregate model coverage.
- `GET /metrics`: recent-window request/error/latency metrics, training runs,
  model RMSE, baseline RMSE, model coverage and telemetry write failures.
- `GET /logs/predict?limit=100`: bounded recent structured prediction events.
- `GET /logs/train`: model training events.

## Docker

```bash
docker build -t country-revenue-api .
docker run --rm -p 8000:8000 country-revenue-api
```

The image build runs the complete test suite, generates deterministic data,
trains country and aggregate models, and renders the plots. A failed test or
pipeline stage fails the image build.

## Peer-Review Evidence

| Requirement | Evidence |
|---|---|
| API unit tests | `tests/revenue/test_revenue_api.py` covers readiness, validation, country, `all`, logs and metrics. |
| Model unit tests | `tests/revenue/test_model.py` covers chronological splitting, comparison, artifacts and deterministic prediction. |
| Logging unit tests | `tests/revenue/test_observability.py` covers training/prediction logs and summaries. |
| Single test script | `python scripts/run-unit-tests.py` runs the complete repository suite. |
| Performance monitoring | `GET /metrics` reports its active-log window, volume, errors, latency, versions, model coverage and latest model RMSE against baseline RMSE. |
| Isolated test I/O | Every read/write test injects `tmp_path` model and log directories with tag `test`; production paths remain untouched. |
| Country and all-country predictions | `POST /predict` accepts a normalized country or the aggregate label `all`. |
| Automated data ingestion | `load_revenue_csv()` validates CSV input; `ml-roadmap-revenue-generate` supplies deterministic automation data. |
| Multiple model comparison | Mean baseline, Ridge and Random Forest use the same chronological holdout and RMSE metric. |
| EDA visualizations | `reports/figures/01_*` through `03_*` show trend, seasonality and country totals. |
| Working Docker image | `Dockerfile` tests, builds artifacts, serves as a non-root user and provides a health check; CI smoke tests it. |
| Baseline comparison visualization | `reports/figures/04_model_vs_baseline_rmse.png` compares selected models with the mean baseline. |

## Leakage And Isolation Controls

- Features use only lagged or rolling historical revenue; the chronological
  holdout prevents future observations entering training.
- Model and log roots are explicit dependencies. Tests write only beneath
  pytest temporary directories.
- Production and test artifacts use separate `prod` and `test` tags.
- Logs exclude raw request bodies while retaining model version, country,
  target date, prediction, status and runtime.
- Active logs rotate under a process lock at a bounded size; log APIs and
  operational metrics explicitly identify their bounded recent window.
- Telemetry write failures are counted without turning a valid prediction into
  an API failure.
