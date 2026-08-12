from __future__ import annotations

import argparse
import json
from pathlib import Path

from ml_roadmap.lab_examples import run_example


def main() -> int:
    parser = argparse.ArgumentParser(description="Run an offline roadmap lab example")
    parser.add_argument("--lab", type=int, required=True, choices=range(0, 20))
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = {"lab": f"lab-{args.lab:02d}", "status": "starter-example-completed", "result": run_example(args.lab)}
    output = args.output or Path(f".artifacts/lab-{args.lab:02d}-evidence.json")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, default=list, ensure_ascii=False, indent=2), encoding="utf-8")
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
