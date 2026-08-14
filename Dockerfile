FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    MPLCONFIGDIR=/tmp/matplotlib \
    REVENUE_DATA_PATH=/app/capstones/country-revenue/data/revenue.csv \
    REVENUE_MODEL_DIR=/app/capstones/country-revenue/models \
    REVENUE_LOG_DIR=/app/capstones/country-revenue/logs \
    REVENUE_TAG=prod

RUN useradd --create-home appuser
WORKDIR /app

COPY requirements.lock pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir -r requirements.lock \
    && pip install --no-cache-dir -e . --no-deps

COPY . .
RUN python scripts/run-unit-tests.py
RUN python -m ml_roadmap.revenue.generate_data \
      --output capstones/country-revenue/data/revenue.csv \
    && python -m ml_roadmap.revenue.train \
      --data capstones/country-revenue/data/revenue.csv \
      --model-dir capstones/country-revenue/models \
      --log-dir capstones/country-revenue/logs \
      --tag prod \
    && python -m ml_roadmap.revenue.eda \
      --data capstones/country-revenue/data/revenue.csv \
      --metrics capstones/country-revenue/models/metrics-prod.json \
      --output-dir capstones/country-revenue/reports/figures \
    && chown -R appuser:appuser capstones/country-revenue

USER appuser
EXPOSE 8000
HEALTHCHECK --interval=15s --timeout=3s --start-period=10s --retries=3 \
  CMD python -c "import json,urllib.request; data=json.load(urllib.request.urlopen('http://127.0.0.1:8000/health',timeout=2)); raise SystemExit(0 if data.get('status') == 'ready' else 1)"

CMD ["uvicorn", "ml_roadmap.revenue.api:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]
