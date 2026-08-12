from pathlib import Path

from ml_roadmap.cv.evaluate import failure_records, per_class_metrics
from ml_roadmap.cv.train import checkpoint_state, select_profile


def test_profile_falls_back_to_cpu() -> None:
    assert select_profile(cuda_available=False) == "cpu-mini"
    assert select_profile(cuda_available=True) == "gpu-free"


def test_checkpoint_round_trip(tmp_path: Path) -> None:
    path = tmp_path / "checkpoint.json"
    checkpoint_state(path, epoch=2, history=[0.8, 0.6], seed=7)
    assert '"epoch": 2' in path.read_text(encoding="utf-8")


def test_failure_and_per_class_metrics() -> None:
    truth = [0, 0, 1, 1]
    predicted = [0, 1, 1, 0]
    metrics = per_class_metrics(truth, predicted, labels=[0, 1])
    failures = failure_records(truth, predicted, ids=["a", "b", "c", "d"])
    assert metrics["macro_f1"] == 0.5
    assert [item["id"] for item in failures] == ["b", "d"]

