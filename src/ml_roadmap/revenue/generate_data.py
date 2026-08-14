from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
import pandas as pd

COUNTRY_BASE_REVENUE = {
    "france": 125.0,
    "germany": 155.0,
    "united_kingdom": 210.0,
    "viet_nam": 105.0,
}


def generate_dataset(
    output_path: Path,
    *,
    days: int = 240,
    seed: int = 42,
) -> pd.DataFrame:
    if days < 30:
        raise ValueError("days must be at least 30")
    rng = np.random.default_rng(seed)
    rows: list[dict[str, object]] = []
    for offset, date in enumerate(pd.date_range("2018-01-01", periods=days)):
        weekly = 12 * np.sin(2 * np.pi * offset / 7)
        monthly = 8 * np.sin(2 * np.pi * offset / 30)
        for index, (country, base) in enumerate(COUNTRY_BASE_REVENUE.items()):
            revenue = base + offset * (0.12 + index * 0.025) + weekly + monthly
            revenue += rng.normal(0, 3 + index)
            rows.append(
                {
                    "date": date.date().isoformat(),
                    "country": country,
                    "revenue": round(max(0.0, float(revenue)), 2),
                }
            )
    frame = pd.DataFrame(rows, columns=["date", "country", "revenue"])
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output_path, index=False, lineterminator="\n")
    return frame


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate deterministic country revenue data")
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--days", type=int, default=240)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    frame = generate_dataset(args.output, days=args.days, seed=args.seed)
    print(f"wrote {len(frame)} rows to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

