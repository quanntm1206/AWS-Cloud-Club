from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

from .data import aggregate_daily, load_revenue_csv


def _save(fig: Any, output_dir: Path, name: str) -> Path:
    path = output_dir / name
    fig.tight_layout()
    fig.savefig(path, dpi=140)
    plt.close(fig)
    return path


def create_plots(data_path: Path, metrics_path: Path, output_dir: Path) -> list[Path]:
    frame = load_revenue_csv(data_path)
    if not metrics_path.is_file():
        raise FileNotFoundError(f"model metrics not found: {metrics_path}")
    metrics = json.loads(metrics_path.read_text(encoding="utf-8"))
    if not isinstance(metrics, list) or not metrics:
        raise ValueError("model metrics must be a non-empty list")
    output_dir.mkdir(parents=True, exist_ok=True)
    paths: list[Path] = []

    daily = aggregate_daily(frame, "all")
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(daily["date"], daily["revenue"], color="#087e8b", linewidth=1.4)
    ax.set(title="Daily Revenue - All Countries", xlabel="Date", ylabel="Revenue")
    paths.append(_save(fig, output_dir, "01_daily_revenue_all.png"))

    monthly = frame.assign(month=frame["date"].dt.month).groupby("month")["revenue"].mean()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.bar(monthly.index, monthly.values, color="#ff5a5f")
    ax.set(title="Average Revenue by Month", xlabel="Month", ylabel="Average revenue")
    paths.append(_save(fig, output_dir, "02_monthly_seasonality.png"))

    totals = frame.groupby("country")["revenue"].sum().sort_values()
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.barh(totals.index, totals.values, color="#f6ae2d")
    ax.set(title="Total Revenue by Country", xlabel="Total revenue", ylabel="Country")
    paths.append(_save(fig, output_dir, "03_revenue_by_country.png"))

    labels = [str(item["country"]) for item in metrics]
    selected = [float(item["rmse"]) for item in metrics]
    baseline = [float(item["baseline_rmse"]) for item in metrics]
    positions = list(range(len(labels)))
    width = 0.38
    fig, ax = plt.subplots(figsize=(10, 4.5))
    ax.bar(
        [position - width / 2 for position in positions],
        baseline,
        width,
        label="Mean baseline",
        color="#6c757d",
    )
    ax.bar(
        [position + width / 2 for position in positions],
        selected,
        width,
        label="Selected model",
        color="#087e8b",
    )
    ax.set_xticks(positions, labels, rotation=25, ha="right")
    ax.set(title="Selected Model vs Baseline", ylabel="RMSE (lower is better)")
    ax.legend()
    paths.append(_save(fig, output_dir, "04_model_vs_baseline_rmse.png"))
    return paths


def main() -> int:
    parser = argparse.ArgumentParser(description="Render country revenue EDA plots")
    parser.add_argument("--data", type=Path, required=True)
    parser.add_argument("--metrics", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    paths = create_plots(args.data, args.metrics, args.output_dir)
    print(f"wrote {len(paths)} plots to {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

