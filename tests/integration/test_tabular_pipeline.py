from pathlib import Path

from ml_roadmap.config import TrainConfig
from ml_roadmap.data import make_demo_churn_data
from ml_roadmap.train_tabular import train


def test_mini_pipeline_beats_dummy_baseline(tmp_path: Path) -> None:
    del tmp_path
    result = train(TrainConfig(target="churn", seed=42), make_demo_churn_data(200, seed=42))
    assert result.metrics["roc_auc"] >= result.metrics["dummy_roc_auc"]
    assert result.metrics["test_rows"] > 0
    assert result.metrics["f1"] > 0
    assert result.metrics["validation_f1"] > 0
    assert result.threshold == result.metrics["selected_threshold"]
