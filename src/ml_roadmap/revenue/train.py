from __future__ import annotations

import argparse
from pathlib import Path
from time import perf_counter
from uuid import uuid4

from .data import load_revenue_csv
from .model import MODEL_VERSION, train_all
from .observability import log_training


def run_training(data_path: Path, model_dir: Path, log_dir: Path, *, tag: str) -> int:
    frame = load_revenue_csv(data_path)
    started = perf_counter()
    results = train_all(frame, model_dir, tag=tag)
    runtime_ms = (perf_counter() - started) * 1000
    run_id = uuid4().hex
    for result in results:
        log_training(
            log_dir,
            country=result.country,
            model_name=result.best_model,
            model_version=MODEL_VERSION,
            rmse=result.rmse,
            baseline_rmse=result.baseline_rmse,
            runtime_ms=runtime_ms,
            run_id=run_id,
            tag=tag,
        )
    return len(results)


def main() -> int:
    parser = argparse.ArgumentParser(description="Train country and combined revenue models")
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--model-dir", type=Path, required=True)
    parser.add_argument("--log-dir", type=Path, required=True)
    parser.add_argument("--tag", default="prod")
    args = parser.parse_args()
    count = run_training(args.data, args.model_dir, args.log_dir, tag=args.tag)
    print(f"trained {count} models in {args.model_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
