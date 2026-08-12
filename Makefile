.PHONY: test lint typecheck check
test:
	python -m pytest -q
lint:
	python -m ruff check .
typecheck:
	python -m mypy
check: lint typecheck test

