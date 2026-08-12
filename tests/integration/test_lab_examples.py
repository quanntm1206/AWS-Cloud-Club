import pytest

from ml_roadmap.lab_examples import run_example


@pytest.mark.parametrize("lab", range(20))
def test_every_offline_lab_has_runnable_domain_example(lab: int) -> None:
    result = run_example(lab)
    assert result


def test_applied_ml_examples_respect_evaluation_boundaries() -> None:
    comparison = run_example(8)
    assert comparison["selected_on"] == "validation"
    assert "final_test_auc" in comparison

    ablation = run_example(9)
    assert ablation["selected_on"] == "validation"
    assert ablation["test_set_touched"] is False

    analysis = run_example(10)
    assert analysis["evaluation_split"] == "held-out-test"
    assert len(analysis["failure_records"]) <= 20
    assert all("support" in metric and "f1" in metric for metric in analysis["slice_metrics"].values())


def test_metrics_and_cv_examples_match_their_scientific_contract() -> None:
    metrics = run_example(6)
    assert metrics["validation_pr_auc"] >= 0
    assert metrics["test_pr_auc"] >= 0
    assert metrics["false_negative_cost"] > metrics["false_positive_cost"]

    cross_validation = run_example(7)
    assert cross_validation["evaluation_scope"] == "development-only; held-out test untouched"
