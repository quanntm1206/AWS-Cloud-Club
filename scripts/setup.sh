#!/usr/bin/env bash
set -euo pipefail
profile="core"
while [[ $# -gt 0 ]]; do
  case "$1" in --profile) profile="$2"; shift 2;; *) echo "Unknown argument: $1"; exit 2;; esac
done
python3 -m venv .venv
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.lock
.venv/bin/python -m pip install -e . --no-deps
if [[ "$profile" == "cv" || "$profile" == "all" ]]; then
  echo "CV dependencies are environment-specific. Follow notebooks/README.md."
fi

