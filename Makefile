.PHONY: test lint typecheck check revenue-build revenue-serve
test:
	python scripts/run-unit-tests.py
lint:
	python -m ruff check .
typecheck:
	python -m mypy
check: lint typecheck test

revenue-build:
	python -m ml_roadmap.revenue.generate_data --output capstones/country-revenue/data/revenue.csv
	python -m ml_roadmap.revenue.train --data capstones/country-revenue/data/revenue.csv --model-dir capstones/country-revenue/models --log-dir capstones/country-revenue/logs --tag prod
	python -m ml_roadmap.revenue.eda --data capstones/country-revenue/data/revenue.csv --metrics capstones/country-revenue/models/metrics-prod.json --output-dir capstones/country-revenue/reports/figures

revenue-serve:
	uvicorn ml_roadmap.revenue.api:create_app --factory --host 0.0.0.0 --port 8000

