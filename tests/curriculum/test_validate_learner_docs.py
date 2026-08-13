from pathlib import Path

import yaml

from scripts.validate_learner_docs import validate


def test_validator_rejects_missing_recovery_guidance(tmp_path: Path) -> None:
    week_dir = tmp_path / "roadmap/weeks"
    lab_dir = tmp_path / "labs"
    week_dir.mkdir(parents=True)
    lab_dir.mkdir(parents=True)
    week = week_dir / "week-01.md"
    week.write_text("# Week 01\n\n| Activity | Hours |\n|---|---:|\n| Study | 9 |\n", encoding="utf-8")

    errors = validate(tmp_path)
    assert any("expected 24 week guides" in error for error in errors)
    assert any("missing ## When you get stuck" in error for error in errors)


def test_glossary_has_beginner_friendly_progression_schema() -> None:
    root = Path(__file__).resolve().parents[2]
    terms = yaml.safe_load((root / "curriculum/glossary.yml").read_text(encoding="utf-8"))["terms"]
    required = {
        "dataset",
        "sample",
        "data split",
        "data validation",
        "validation set",
        "model validation",
        "augmentation",
        "epoch",
        "batch",
        "loss",
        "optimizer",
        "preprocessing",
        "transform",
        "parameter",
        "hyperparameter",
        "backbone",
        "freeze",
        "fine-tuning",
    }
    by_term = {item["term"]: item for item in terms}
    assert required <= by_term.keys()
    assert len(terms) >= 50
    for item in terms:
        assert {"term", "meaning", "example", "introduced_in"} <= item.keys()
        assert item["meaning"] and item["example"]
        assert 0 <= item["introduced_in"] <= 20


def test_each_lab_contract_uses_english_labels(tmp_path: Path) -> None:
    glossary_dir = tmp_path / "curriculum"
    lab_dir = tmp_path / "labs/lab-00-demo"
    expected_dir = lab_dir / "expected"
    glossary_dir.mkdir(parents=True)
    expected_dir.mkdir(parents=True)
    (glossary_dir / "glossary.yml").write_text(
        yaml.safe_dump(
            {"terms": [{"term": "dataset", "meaning": "m", "example": "e", "introduced_in": 0}]},
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    (lab_dir / "README.md").write_text(
        """# Lab 00

## Terms used in this lab

**New terms:** `dataset`

**Review:** None - this is the first lab.

**Use in this lab:** Count rows in the `dataset`.

**Explain it yourself:** What is a dataset?
""",
        encoding="utf-8",
    )
    (expected_dir / "README.md").write_text("## Terminology oracle\n", encoding="utf-8")
    assert validate(tmp_path, require_complete=False) == []


def test_every_week_and_expected_receipt_reinforces_vocabulary() -> None:
    root = Path(__file__).resolve().parents[2]
    for week in range(1, 25):
        text = (root / f"roadmap/weeks/week-{week:02d}.md").read_text(encoding="utf-8")
        assert "## Keywords for this week" in text
        assert "**Review:**" in text
        assert "**Use:**" in text


def test_validator_rejects_decorative_or_future_terms(tmp_path: Path) -> None:
    glossary_dir = tmp_path / "curriculum"
    lab_dir = tmp_path / "labs/lab-00-demo"
    expected_dir = lab_dir / "expected"
    glossary_dir.mkdir(parents=True)
    expected_dir.mkdir(parents=True)
    (glossary_dir / "glossary.yml").write_text(
        yaml.safe_dump(
            {
                "terms": [
                    {"term": "dataset", "meaning": "m", "example": "e", "introduced_in": 0},
                    {"term": "augmentation", "meaning": "m", "example": "e", "introduced_in": 1},
                ]
            },
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    (lab_dir / "README.md").write_text(
        """# Lab 00

## Terms used in this lab

**New terms:** `dataset`, `augmentation`

**Review:** None - this is the first lab.

**Use in this lab:** Count the rows.

**Explain it yourself:** What is a dataset?
""",
        encoding="utf-8",
    )
    (expected_dir / "README.md").write_text("# Expected\n", encoding="utf-8")
    errors = validate(tmp_path, require_complete=False)
    assert any("introduced in a future lab" in error for error in errors)
    assert any("application must use term" in error for error in errors)


def test_validator_scans_full_lab_for_terms_used_before_introduction(tmp_path: Path) -> None:
    glossary_dir = tmp_path / "curriculum"
    lab_dir = tmp_path / "labs/lab-00-demo"
    expected_dir = lab_dir / "expected"
    glossary_dir.mkdir(parents=True)
    expected_dir.mkdir(parents=True)
    (glossary_dir / "glossary.yml").write_text(
        yaml.safe_dump(
            {
                "terms": [
                    {"term": "dataset", "meaning": "m", "example": "e", "introduced_in": 0},
                    {"term": "checkpoint", "meaning": "m", "example": "e", "introduced_in": 2},
                ]
            },
            allow_unicode=True,
        ),
        encoding="utf-8",
    )
    (lab_dir / "README.md").write_text(
        """# Lab 00

## Objective
    Create a `checkpoint` too early.
## Terms used in this lab
**New terms:** `dataset`
**Review:** None - this is the first lab.
**Use in this lab:** Count samples in the `dataset`.
**Explain it yourself:** What is a dataset?
## Before you begin
Local.
## Completion criteria
The count is correct.
## When you get stuck
Print the data.
""",
        encoding="utf-8",
    )
    (expected_dir / "README.md").write_text("## Terminology oracle\n", encoding="utf-8")
    errors = validate(tmp_path, require_complete=False)
    assert any("uses term checkpoint before lab 2" in error for error in errors)
