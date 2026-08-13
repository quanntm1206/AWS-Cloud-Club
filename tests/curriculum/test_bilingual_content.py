import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
DOCX_VI = ROOT / "docs/docx-vi"


def _load_yaml(path: Path) -> dict:
    return yaml.safe_load(path.read_text(encoding="utf-8"))


def test_github_learner_guides_use_the_english_contract() -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "Machine Learning Engineer Roadmap" in readme

    weeks = sorted((ROOT / "roadmap/weeks").glob("week-*.md"))
    labs = sorted((ROOT / "labs").glob("lab-[0-9][0-9]-*/README.md"))
    assert len(weeks) == 24
    assert len(labs) == 21
    for path in weeks:
        text = path.read_text(encoding="utf-8")
        assert "## Why this week matters" in text
        assert "## Keywords for this week" in text
        assert "## Signs that you understand" in text
        assert "## When you get stuck" in text
    for path in labs:
        text = path.read_text(encoding="utf-8")
        assert "## Terms used in this lab" in text
        assert "**New terms:**" in text
        assert "**Review:**" in text
        assert "**Use in this lab:**" in text
        assert "**Explain it yourself:**" in text


def test_learner_guides_do_not_keep_vietnamese_instructional_headings() -> None:
    roots = [
        ROOT / "README.md",
        ROOT / "roadmap",
        ROOT / "labs",
        ROOT / "notebooks",
        ROOT / "capstones",
        ROOT / "aws/README.md",
        ROOT / "docs/source-notes",
        ROOT / "curriculum",
    ]
    paths: list[Path] = []
    for root in roots:
        paths.extend([root] if root.is_file() else root.rglob("*"))
    markers = re.compile(
        r"^#{1,6} Vì sao tuần này quan trọng\s*$|^#{1,6} Từ khóa tuần này\s*$|"
        r"^#{1,6} Dấu hiệu bạn đã hiểu\s*$|^#{1,6} Khi mắc kẹt\s*$|"
        r"^#{1,6} Thuật ngữ trong lab\s*$|^\*\*Thuật ngữ mới:\*\*|^\*\*Ôn lại:\*\*|"
        r"^\*\*Áp dụng trong lab:\*\*|^\*\*Tự giải thích:\*\*|"
        r"^#{1,6} Mục tiêu(?: tuần)?\s*$|^#{1,6} Trước khi bắt đầu\s*$|"
        r"^#{1,6} Khi nào xem như hoàn thành\s*$|^#{1,6} Oracle thuật ngữ\s*$",
        re.MULTILINE,
    )
    offenders = [
        path.relative_to(ROOT).as_posix()
        for path in paths
        if path.is_file()
        and path.suffix.lower() in {".md", ".yml", ".yaml", ".ipynb"}
        and markers.search(path.read_text(encoding="utf-8"))
    ]
    assert offenders == []


def test_vietnamese_docx_sources_are_complete_and_aligned() -> None:
    vi_curriculum = _load_yaml(DOCX_VI / "curriculum/curriculum.yml")
    en_curriculum = _load_yaml(ROOT / "curriculum/curriculum.yml")
    assert [week["id"] for week in vi_curriculum["weeks"]] == [
        week["id"] for week in en_curriculum["weeks"]
    ]
    assert [week["lab"] for week in vi_curriculum["weeks"]] == [
        week["lab"] for week in en_curriculum["weeks"]
    ]

    vi_glossary = _load_yaml(DOCX_VI / "curriculum/glossary.yml")["terms"]
    en_glossary = _load_yaml(ROOT / "curriculum/glossary.yml")["terms"]
    assert [(item["term"], item["introduced_in"]) for item in vi_glossary] == [
        (item["term"], item["introduced_in"]) for item in en_glossary
    ]
    assert any("Tập dữ liệu" in item["meaning"] for item in vi_glossary)

    vi_weeks = sorted((DOCX_VI / "roadmap/weeks").glob("week-*.md"))
    assert len(vi_weeks) == 24
    for path in vi_weeks:
        text = path.read_text(encoding="utf-8")
        assert "## Vì sao tuần này quan trọng" in text
        assert "## Từ khóa tuần này" in text
        assert "## Khi mắc kẹt" in text


def test_docx_builder_reads_prose_only_from_vietnamese_sources() -> None:
    builder = (ROOT / "scripts/build_docx.py").read_text(encoding="utf-8")
    assert 'DOCX_VI = ROOT / "docs/docx-vi"' in builder
    assert 'ROOT / "curriculum/curriculum.yml"' not in builder
    assert 'ROOT / "curriculum/assessment.yml"' not in builder
    assert 'ROOT / "curriculum/glossary.yml"' not in builder
    assert 'ROOT / f"roadmap/weeks/' not in builder
