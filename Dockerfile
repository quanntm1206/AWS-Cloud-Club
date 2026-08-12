FROM python:3.12-slim
RUN useradd --create-home appuser
WORKDIR /app
COPY pyproject.toml README.md ./
COPY src ./src
RUN pip install --no-cache-dir ".[serve]"
USER appuser
EXPOSE 8000
CMD ["uvicorn", "ml_roadmap.api:create_app", "--factory", "--host", "0.0.0.0", "--port", "8000"]

