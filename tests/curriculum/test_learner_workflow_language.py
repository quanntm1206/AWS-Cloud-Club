import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
WEEK_FILES = sorted((ROOT / "roadmap/weeks").glob("week-*.md"))
MILESTONE_FILES = sorted((ROOT / "roadmap/checkpoints").glob("checkpoint-*.md"))
LEARNER_WORKFLOW_FILES = [ROOT / "README.md", ROOT / "labs/README.md"]
LEARNER_WORKFLOW_FILES.extend(sorted((ROOT / "labs").glob("lab-*/README.md")))
LEARNER_WORKFLOW_FILES.extend(sorted((ROOT / "labs").glob("lab-*/expected/README.md")))
LEARNER_WORKFLOW_FILES.extend(sorted((ROOT / "capstones").glob("*/README.md")))


def test_week_guides_use_local_first_terminology() -> None:
    assert len(WEEK_FILES) == 24
    for path in WEEK_FILES:
        text = path.read_text(encoding="utf-8")
        assert text.count("## Mục tiêu tuần") == 1, path.name
        assert "## Kết quả đầu ra" not in text, path.name
        assert text.count("## Kết quả hướng tới") == 1, path.name
        assert "## Deliverable GitHub" not in text, path.name
        assert text.count("Learning log và tự đánh giá") == 1, path.name
        assert "Learning log và GitHub" not in text, path.name
        assert not re.search(r"\bdeliverable\b", text, flags=re.IGNORECASE), path.name


def test_milestone_guides_use_self_assessment_terminology() -> None:
    assert len(MILESTONE_FILES) == 6
    for index, path in enumerate(MILESTONE_FILES, start=1):
        text = path.read_text(encoding="utf-8")
        assert text.startswith(f"# Mốc năng lực {index:02d} - Tuần {index * 4}")
        assert text.count("## Minh chứng đạt mốc") == 1, path.name
        assert "## Nộp" not in text, path.name
        assert "commit/tag checkpoint" not in text.lower(), path.name
        assert "tự đánh giá" in text.lower(), path.name
        assert "lưu cục bộ" in text.lower(), path.name


def test_learner_facing_docs_do_not_require_github_workflow() -> None:
    paths = [ROOT / "README.md", ROOT / "roadmap/00-getting-started.md"]
    for directory in ("roadmap/weeks", "roadmap/checkpoints", "labs", "capstones"):
        paths.extend(sorted((ROOT / directory).rglob("*.md")))

    banned_patterns = {
        "Nộp GitHub": r"nộp github",
        "Portfolio GitHub": r"portfolio github",
        "fork repo": r"\bfork (?:repo|repository)\b",
        "push": r"(?:\bgit push\b|\bpush (?:lên|to)\b)",
        "pull request": r"\bpull request\b",
        "commit mỗi tuần": r"\bcommit mỗi tuần\b",
        "submission": r"\bsubmission\b",
    }
    for path in paths:
        text = path.read_text(encoding="utf-8")
        if path == ROOT / "README.md":
            text = text.replace(
                "Người học không fork, commit, push, mở pull request hoặc nộp bài.", ""
            )
        for label, pattern in banned_patterns.items():
            assert not re.search(pattern, text, flags=re.IGNORECASE), f"{path.relative_to(ROOT)}: {label}"


def test_getting_started_defines_github_as_clone_only() -> None:
    text = (ROOT / "roadmap/00-getting-started.md").read_text(encoding="utf-8")
    assert "GitHub chỉ dùng để clone" in text
    assert "không nộp bài" in text.lower()


def test_readme_defines_owner_template_clone_and_local_artifacts() -> None:
    text = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "git clone https://github.com/quanntm1206/AWS-Cloud-Club.git" in text
    assert "<REPO_URL>" not in text
    assert "không fork, commit, push, mở pull request hoặc nộp bài" in text.lower()
    assert "lưu cục bộ" in text.lower()


def test_labs_and_capstones_keep_evidence_local() -> None:
    for path in LEARNER_WORKFLOW_FILES:
        text = path.read_text(encoding="utf-8")
        assert "local" in text.lower() or "cục bộ" in text.lower(), path.relative_to(ROOT)


def test_design_uses_local_self_assessment_decision() -> None:
    text = (ROOT / "docs/superpowers/specs/2026-08-12-ml-engineer-roadmap-design.md").read_text(
        encoding="utf-8"
    )
    for term in ("Kết quả hướng tới", "Mốc năng lực", "Minh chứng đạt mốc", "Tổng kết năng lực"):
        assert term in text
    assert "portfolio GitHub" not in text
    assert "sản phẩm GitHub" not in text
    assert "checkpoint mỗi epoch" in text


def test_ml_checkpoint_terms_remain_technical() -> None:
    week_19 = (ROOT / "roadmap/weeks/week-19.md").read_text(encoding="utf-8")
    notebook = (ROOT / "notebooks/colab/cv_transfer_learning_colab.ipynb").read_text(encoding="utf-8")

    assert "Checkpoint/resume" in week_19
    assert "checkpoint artifact" in week_19
    assert "checkpoint.pt" in notebook
