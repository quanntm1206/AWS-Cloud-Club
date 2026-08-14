import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
EN_GLOSSARY = ROOT / "curriculum/glossary.yml"
VI_GLOSSARY = ROOT / "docs/docx-vi/curriculum/glossary.yml"
GLOSSARY_FIELDS = {
    "term",
    "meaning",
    "why_it_matters",
    "example",
    "common_confusion",
    "self_check",
    "introduced_in",
}
EXPLANATION_FIELDS = GLOSSARY_FIELDS - {"term", "introduced_in"}
PLACEHOLDER = re.compile(r"\b(?:TODO|TBD|FIXME|lorem ipsum|placeholder)\b|<[^>]+>", re.IGNORECASE)


def _yaml_terms(path: Path) -> list[dict]:
    return yaml.safe_load(path.read_text(encoding="utf-8"))["terms"]


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    assert marker in text
    return text.split(marker, 1)[1].split("\n## ", 1)[0].strip()


def _field(text: str, label: str) -> str:
    marker = f"**{label}:**"
    assert marker in text
    return text.split(marker, 1)[1].splitlines()[0].strip()


def _terms(value: str) -> list[str]:
    return [part for index, part in enumerate(value.split("`")) if index % 2 == 1]


def _groups(section: str) -> list[str]:
    return [group.strip() for group in re.split(r"(?m)^###\s+", section)[1:] if group.strip()]


def _sentence_count(value: str) -> int:
    return len([part for part in re.split(r"(?<=[.!?])\s+", value.strip()) if part])


def _normalized(value: str) -> str:
    return re.sub(r"\s+", " ", value.strip().casefold())


def test_bilingual_glossaries_have_the_deep_term_schema() -> None:
    english = _yaml_terms(EN_GLOSSARY)
    vietnamese = _yaml_terms(VI_GLOSSARY)
    assert len(english) == len(vietnamese) == 78
    assert [(item["term"], item["introduced_in"]) for item in english] == [
        (item["term"], item["introduced_in"]) for item in vietnamese
    ]
    for items in (english, vietnamese):
        for item in items:
            assert set(item) == GLOSSARY_FIELDS, item["term"]
            for field in GLOSSARY_FIELDS - {"introduced_in"}:
                assert str(item[field]).strip(), (item["term"], field)
                assert not PLACEHOLDER.search(str(item[field])), (item["term"], field)
            assert 2 <= _sentence_count(str(item["meaning"])) <= 3, item["term"]
            assert _normalized(str(item["why_it_matters"])) not in _normalized(str(item["meaning"])), item["term"]
            assert str(item["self_check"]).rstrip().endswith("?"), item["term"]
        for field in EXPLANATION_FIELDS:
            values = [_normalized(str(item[field])) for item in items]
            assert len(values) == len(set(values)), f"repeated generic glossary field: {field}"
        self_check_stems = Counter(" ".join(_normalized(str(item["self_check"])).split()[:3]) for item in items)
        assert self_check_stems.most_common(1)[0][1] <= 12, self_check_stems.most_common(1)[0]


def test_english_glossary_markdown_is_generated_and_current() -> None:
    result = subprocess.run(
        [sys.executable, "scripts/build_glossary_markdown.py", "--check"],
        cwd=ROOT,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    text = (ROOT / "roadmap/glossary.md").read_text(encoding="utf-8")
    assert "# Machine Learning Glossary" in text
    for item in _yaml_terms(EN_GLOSSARY):
        assert f"## `{item['term']}`" in text
        assert item["self_check"] in text


def test_all_week_guides_teach_and_reconnect_terms() -> None:
    english_weeks = sorted((ROOT / "roadmap/weeks").glob("week-*.md"))
    vietnamese_weeks = sorted((ROOT / "docs/docx-vi/roadmap/weeks").glob("week-*.md"))
    assert len(english_weeks) == len(vietnamese_weeks) == 24

    english_labels = ("Mental model", "Why it matters", "Worked example", "Easy to confuse", "Check yourself")
    vietnamese_labels = ("Cách hình dung", "Vì sao quan trọng", "Ví dụ xuyên suốt", "Dễ nhầm với", "Tự kiểm tra")
    concept_sections: list[str] = []
    for english_path, vietnamese_path in zip(english_weeks, vietnamese_weeks, strict=True):
        english = english_path.read_text(encoding="utf-8")
        vietnamese = vietnamese_path.read_text(encoding="utf-8")
        concept = _section(english, "Concept walkthrough")
        connection = _section(english, "Connect earlier terms")
        vi_concept = _section(vietnamese, "Giải thích khái niệm")
        vi_connection = _section(vietnamese, "Kết nối kiến thức cũ")
        assert 2 <= len(re.findall(r"^### ", concept, re.MULTILINE)) <= 4
        assert 2 <= len(re.findall(r"^### ", vi_concept, re.MULTILINE)) <= 4
        for label in english_labels:
            assert concept.count(f"**{label}:**") >= 2
        for label in vietnamese_labels:
            assert vi_concept.count(f"**{label}:**") >= 2

        keywords = _section(english, "Keywords for this week")
        vi_keywords = _section(vietnamese, "Từ khóa tuần này")
        focus_terms = _terms(_field(keywords, "New or focus terms"))
        review_terms = _terms(_field(keywords, "Review"))
        vi_focus_terms = _terms(_field(vi_keywords, "Thuật ngữ mới hoặc trọng tâm"))
        vi_review_terms = _terms(_field(vi_keywords, "Ôn lại"))
        assert vi_focus_terms == focus_terms, english_path.name
        assert vi_review_terms == review_terms, english_path.name
        for term in focus_terms:
            assert f"`{term}`" in concept, (english_path.name, term)
            assert f"`{term}`" in vi_concept, (vietnamese_path.name, term)
        for term in review_terms:
            assert f"`{term}`" in connection, (english_path.name, term)
            assert f"`{term}`" in vi_connection, (vietnamese_path.name, term)
        concept_sections.append(re.sub(r"\s+", " ", concept).strip().lower())
    assert len(concept_sections) == len(set(concept_sections))


def test_all_labs_apply_new_and_review_terms() -> None:
    labs = sorted((ROOT / "labs").glob("lab-[0-9][0-9]-*/README.md"))
    assert len(labs) == 21
    application_sections: list[str] = []
    evidence_values: list[str] = []
    for path in labs:
        text = path.read_text(encoding="utf-8")
        terms_section = _section(text, "Terms used in this lab")
        application = _section(text, "Apply the concepts")
        expected_terms = _terms(_field(terms_section, "New terms")) + _terms(_field(terms_section, "Review"))
        applied_terms: list[str] = []
        groups = _groups(application)
        assert groups
        for group in groups:
            body = "\n".join(group.splitlines()[1:])
            for label in (
                "Terms",
                "What they mean here",
                "Where you will see them",
                "Common mistake",
                "Evidence to keep",
                "Explain after the lab",
            ):
                value = _field(body, label)
                assert value, (path.parent.name, group.splitlines()[0], label)
                assert not PLACEHOLDER.search(value), (path.parent.name, group.splitlines()[0], label)
            applied_terms.extend(_terms(_field(body, "Terms")))
            evidence_values.append(_normalized(_field(body, "Evidence to keep")))
        assert len(applied_terms) == len(set(applied_terms)), path.parent.name
        assert set(applied_terms) == set(expected_terms), path.parent.name
        for label in (
            "Terms",
            "What they mean here",
            "Where you will see them",
            "Common mistake",
            "Evidence to keep",
            "Explain after the lab",
        ):
            assert f"**{label}:**" in application, (path.parent.name, label)
        for term in _terms(_field(terms_section, "New terms")):
            assert f"`{term}`" in application, (path.parent.name, term)
        for term in _terms(_field(terms_section, "Review")):
            assert f"`{term}`" in application, (path.parent.name, term)
        application_sections.append(re.sub(r"\s+", " ", application).strip().lower())
    assert len(application_sections) == len(set(application_sections))
    assert len(evidence_values) == len(set(evidence_values))


def test_terminology_oracles_include_reasoning_evidence_and_misconceptions() -> None:
    expected_files = sorted((ROOT / "labs").glob("lab-[0-9][0-9]-*/expected/README.md"))
    assert len(expected_files) == 21
    oracle_sections: list[str] = []
    for path in expected_files:
        full_text = path.read_text(encoding="utf-8")
        text = _section(full_text, "Terminology oracle")
        for label in ("Expected reasoning", "Evidence mapping", "Misconception check"):
            value = _field(text, label)
            assert value, (path.parent.parent.name, label)
            assert not PLACEHOLDER.search(value), (path.parent.parent.name, label)
        assert "status=starter-example-completed" not in _field(text, "Evidence mapping")
        if "status=starter-example-completed" in full_text:
            lab_text = (path.parent.parent / "README.md").read_text(encoding="utf-8")
            assert "does **not** mean that you met all acceptance criteria" in lab_text
        oracle_sections.append(_normalized(text))
    assert len(oracle_sections) == len(set(oracle_sections))
