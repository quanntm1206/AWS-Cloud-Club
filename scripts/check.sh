#!/usr/bin/env bash
set -euo pipefail
scope="all"; profile="mini"
while [[ $# -gt 0 ]]; do
  case "$1" in --scope) scope="$2"; shift 2;; --profile) profile="$2"; shift 2;; *) echo "Unknown argument: $1"; exit 2;; esac
done
python_bin="python3"; [[ -x .venv/bin/python ]] && python_bin=".venv/bin/python"
if [[ "$scope" == "bootstrap" ]]; then "$python_bin" -c 'import ml_roadmap; print(ml_roadmap.__version__)'; exit; fi
"$python_bin" scripts/validate_curriculum.py
"$python_bin" scripts/validate_learner_docs.py
"$python_bin" scripts/build_glossary_markdown.py --check
"$python_bin" scripts/validate_sources.py
"$python_bin" scripts/validate_notebooks.py
"$python_bin" scripts/validate_aws_safety.py
"$python_bin" -m pytest -q
[[ "$scope" != "all" ]] || "$python_bin" -m ruff check .
[[ "$profile" == "mini" ]] || "$python_bin" -m mypy
