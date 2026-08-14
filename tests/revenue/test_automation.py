from pathlib import Path

import pandas as pd

from ml_roadmap.revenue.eda import create_plots
from ml_roadmap.revenue.generate_data import generate_dataset
from ml_roadmap.revenue.model import train_all
from ml_roadmap.revenue.observability import summarize_performance
from ml_roadmap.revenue.train import run_training


def test_generated_dataset_is_deterministic_and_ingestible(tmp_path: Path) -> None:
    first = tmp_path / "first.csv"
    second = tmp_path / "second.csv"

    first_frame = generate_dataset(first, days=45, seed=17)
    second_frame = generate_dataset(second, days=45, seed=17)

    pd.testing.assert_frame_equal(first_frame, second_frame)
    assert first.read_bytes() == second.read_bytes()
    assert list(first_frame.columns) == ["date", "country", "revenue"]
    assert first_frame["country"].nunique() == 4
    assert len(first_frame) == 45 * 4


def test_eda_writes_visualizations_including_baseline_comparison(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    frame = generate_dataset(data_path, days=75, seed=42)
    model_dir = tmp_path / "models"
    train_all(frame, model_dir, tag="eda")

    paths = create_plots(data_path, model_dir / "metrics-eda.json", tmp_path / "plots")

    assert [path.name for path in paths] == [
        "01_daily_revenue_all.png",
        "02_monthly_seasonality.png",
        "03_revenue_by_country.png",
        "04_model_vs_baseline_rmse.png",
    ]
    assert all(path.is_file() and path.stat().st_size > 1_000 for path in paths)


def test_training_entrypoint_writes_models_metrics_and_isolated_logs(tmp_path: Path) -> None:
    data_path = tmp_path / "revenue.csv"
    generate_dataset(data_path, days=60, seed=42)

    count = run_training(
        data_path,
        tmp_path / "models",
        tmp_path / "logs",
        tag="test",
    )

    assert count == 5
    assert (tmp_path / "models" / "model-all-test.joblib").is_file()
    assert (tmp_path / "models" / "metrics-test.json").is_file()
    assert (tmp_path / "logs" / "train-test.jsonl").is_file()
    assert not (tmp_path / "logs" / "train-prod.jsonl").exists()
    assert summarize_performance(tmp_path / "logs", tag="test")["training_run_count"] == 1
