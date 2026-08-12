from pathlib import Path

from scripts.validate_learner_docs import validate


def test_learner_docs_contract_passes() -> None:
    assert validate() == []


def test_validator_rejects_missing_recovery_guidance(tmp_path: Path) -> None:
    week_dir = tmp_path / "roadmap/weeks"
    lab_dir = tmp_path / "labs"
    week_dir.mkdir(parents=True)
    lab_dir.mkdir(parents=True)
    week = week_dir / "week-01.md"
    week.write_text("# Tuần 01\n\n| Hoạt động | Giờ |\n|---|---:|\n| Học | 9 |\n", encoding="utf-8")

    errors = validate(tmp_path)
    assert any("expected 24 week guides" in error for error in errors)
    assert any("missing ## Khi mắc kẹt" in error for error in errors)
