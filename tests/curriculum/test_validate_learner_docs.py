from pathlib import Path

import yaml

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


def test_each_lab_uses_new_terms_and_reviews_prior_terms() -> None:
    root = Path(__file__).resolve().parents[2]
    terms = yaml.safe_load((root / "curriculum/glossary.yml").read_text(encoding="utf-8"))["terms"]
    introduced = {item["term"]: item["introduced_in"] for item in terms}
    for lab in range(21):
        path = next((root / "labs").glob(f"lab-{lab:02d}-*/README.md"))
        text = path.read_text(encoding="utf-8")
        assert "## Thuật ngữ trong lab" in text
        assert "**Thuật ngữ mới:**" in text
        assert "**Áp dụng trong lab:**" in text
        assert "**Tự giải thích:**" in text
        if lab == 0:
            assert "**Ôn lại:** Chưa có" in text
        else:
            assert "**Ôn lại:**" in text and "**Ôn lại:** Chưa có" not in text
        for term, first_lab in introduced.items():
            if first_lab == lab:
                assert f"`{term}`" in text, f"{path.parent.name}: missing introduced term {term}"


def test_every_week_and_expected_receipt_reinforces_vocabulary() -> None:
    root = Path(__file__).resolve().parents[2]
    for week in range(1, 25):
        text = (root / f"roadmap/weeks/week-{week:02d}.md").read_text(encoding="utf-8")
        assert "## Từ khóa tuần này" in text
        assert "**Ôn lại:**" in text
        assert "**Áp dụng:**" in text
    for lab in range(21):
        path = next((root / "labs").glob(f"lab-{lab:02d}-*/expected/README.md"))
        text = path.read_text(encoding="utf-8")
        assert "## Oracle thuật ngữ" in text
        section = text.split("## Oracle thuật ngữ", 1)[1].split("##", 1)[0]
        assert len(section) >= 180
    oracle_sections = [
        next((root / "labs").glob(f"lab-{lab:02d}-*/expected/README.md"))
        .read_text(encoding="utf-8")
        .split("## Oracle thuật ngữ", 1)[1]
        .split("##", 1)[0]
        for lab in range(21)
    ]
    assert len(set(oracle_sections)) == 21


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

## Thuật ngữ trong lab

**Thuật ngữ mới:** `dataset`, `augmentation`

**Ôn lại:** Chưa có - đây là lab đầu tiên.

**Áp dụng trong lab:** Đếm số hàng.

**Tự giải thích:** Dataset là gì?
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

## Mục tiêu
Tạo checkpoint sớm.
## Thuật ngữ trong lab
**Thuật ngữ mới:** `dataset`
**Ôn lại:** Chưa có - đây là lab đầu tiên.
**Áp dụng trong lab:** Đếm sample trong `dataset`.
**Tự giải thích:** Dataset là gì?
## Trước khi bắt đầu
Local.
## Khi nào xem như hoàn thành
Đếm đúng.
## Khi mắc kẹt
In dữ liệu.
""",
        encoding="utf-8",
    )
    (expected_dir / "README.md").write_text("## Oracle thuật ngữ\n", encoding="utf-8")
    errors = validate(tmp_path, require_complete=False)
    assert any("uses term checkpoint before lab 2" in error for error in errors)
