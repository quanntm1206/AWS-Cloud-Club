from pathlib import Path

import yaml

from scripts.validate_curriculum import validate

ROOT = Path(__file__).resolve().parents[2]


def test_curriculum_contract_passes() -> None:
    assert validate() == []


def test_validator_rejects_out_of_range_workload(tmp_path: Path) -> None:
    source = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    source["weeks"][0]["hours"] = 11
    path = tmp_path / "curriculum.yml"
    path.write_text(yaml.safe_dump(source), encoding="utf-8")
    assert any("workload" in error for error in validate(path))


def test_validator_rejects_early_aws_requirement(tmp_path: Path) -> None:
    source = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    source["weeks"][0]["environments"].append("aws")
    path = tmp_path / "curriculum.yml"
    path.write_text(yaml.safe_dump(source), encoding="utf-8")
    assert any("cannot require AWS" in error for error in validate(path))


def test_validator_rejects_milestones_on_wrong_weeks(tmp_path: Path) -> None:
    source = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    source["weeks"][2]["milestone"] = "milestone-01"
    source["weeks"][3].pop("checkpoint", None)
    source["weeks"][3]["milestone"] = None
    path = tmp_path / "curriculum.yml"
    path.write_text(yaml.safe_dump(source), encoding="utf-8")
    assert any("six ordered milestones" in error for error in validate(path))


def test_curriculum_and_assessment_use_milestone_schema() -> None:
    curriculum = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    assessment = yaml.safe_load((ROOT / "curriculum/assessment.yml").read_text(encoding="utf-8"))

    assert all("checkpoint" not in week for week in curriculum["weeks"])
    assert [week["id"] for week in curriculum["weeks"] if week["milestone"]] == [4, 8, 12, 16, 20, 24]
    assert [week["milestone"] for week in curriculum["weeks"] if week["milestone"]] == [
        f"milestone-{index:02d}" for index in range(1, 7)
    ]
    assert "checkpoints" not in assessment
    assert [milestone["id"] for milestone in assessment["milestones"]] == [
        f"milestone-{index:02d}" for index in range(1, 7)
    ]
    assert [milestone["weeks"] for milestone in assessment["milestones"]] == [4, 8, 12, 16, 20, 24]


def test_all_week_and_checkpoint_docs_exist() -> None:
    for week in range(1, 25):
        assert (ROOT / f"roadmap/weeks/week-{week:02d}.md").exists()
    for checkpoint in range(1, 7):
        assert (ROOT / f"roadmap/checkpoints/checkpoint-{checkpoint:02d}.md").exists()


def test_all_declared_labs_have_guides() -> None:
    data = yaml.safe_load((ROOT / "curriculum/curriculum.yml").read_text(encoding="utf-8"))
    for lab in {week["lab"] for week in data["weeks"]}:
        assert list((ROOT / "labs").glob(f"{lab}-*/README.md")), f"missing {lab}"


def test_week_guides_have_topic_specific_teaching() -> None:
    generic = "Frame the problem before choosing a model; build a baseline before tuning."
    required_sections = ["Core knowledge", "Guided practice", "Test yourself", "Common errors"]
    for week in range(1, 25):
        text = (ROOT / f"roadmap/weeks/week-{week:02d}.md").read_text(encoding="utf-8")
        assert generic not in text
        for section in required_sections:
            body = text.split(f"## {section}", 1)[1].split("##", 1)[0].strip()
            assert len(body.splitlines()) >= 2, f"week {week}: {section} is too thin"


def test_offline_labs_reference_real_runner_from_repo_root() -> None:
    for lab in range(20):
        guide = next((ROOT / "labs").glob(f"lab-{lab:02d}-*/README.md"))
        text = guide.read_text(encoding="utf-8")
        assert f"scripts/run_lab.py --lab {lab}" in text
        assert f".venv/bin/python scripts/run_lab.py --lab {lab}" in text
        assert "status=starter-example-completed" in text
    assert "acceptance" in text.lower()


def test_docker_lab_documents_real_smoke_commands() -> None:
    text = (ROOT / "labs/lab-15-docker-and-ci/README.md").read_text(encoding="utf-8")
    for command in ("docker build", "docker run", "docker logs", "docker stop", "/health", "/predict"):
        assert command in text
    assert "not root" in text


def test_aws_lab_has_powershell_and_bash_lifecycle_commands() -> None:
    text = (ROOT / "labs/lab-20-aws-safe-lifecycle/README.md").read_text(encoding="utf-8")
    assert "```powershell" in text and "```bash" in text
    for script in ("cost-check", "preflight", "deploy", "cleanup", "residual-scan"):
        assert f"aws/scripts/{script}.ps1" in text
        assert f"aws/scripts/{script}.sh" in text


def test_expected_receipts_are_lab_specific() -> None:
    for lab in range(21):
        directory = next((ROOT / "labs").glob(f"lab-{lab:02d}-*"))
        text = (directory / "expected/README.md").read_text(encoding="utf-8")
        assert directory.name in text
        assert "## Oracle" in text and "## Required receipt" in text
        assert "describe the oracle and expected evidence format" not in text


def test_repo_documents_all_21_labs() -> None:
    lab_directories = sorted((ROOT / "labs").glob("lab-[0-9][0-9]-*"))
    assert len(lab_directories) == 21
    assert lab_directories[0].name.startswith("lab-00-")
    assert lab_directories[-1].name.startswith("lab-20-")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    labs_readme = (ROOT / "labs/README.md").read_text(encoding="utf-8")
    assert "21 lab" in readme
    assert "lab-00" in labs_readme and "lab-20" in labs_readme


def test_week_guides_fit_the_stated_weekly_budget() -> None:
    for week in range(1, 25):
        text = (ROOT / f"roadmap/weeks/week-{week:02d}.md").read_text(encoding="utf-8")
        rows = []
        for line in text.splitlines():
            if line.startswith("|") and line.count("|") >= 3:
                value = line.split("|")[-2].strip()
                if value.isdigit():
                    rows.append(int(value))
        assert 8 <= sum(rows) <= 10, f"week {week}: schedule totals {sum(rows)} hours"


def test_week_guides_offer_context_and_recovery() -> None:
    for week in range(1, 25):
        text = (ROOT / f"roadmap/weeks/week-{week:02d}.md").read_text(encoding="utf-8")
        assert "## Why this week matters" in text, f"week {week}"
        assert "## When you get stuck" in text, f"week {week}"
        assert "## Signs that you understand" in text, f"week {week}"


def test_lab_guides_use_truthful_english_learning_contract() -> None:
    for lab in range(20):
        guide = next((ROOT / "labs").glob(f"lab-{lab:02d}-*/README.md"))
        text = guide.read_text(encoding="utf-8")
        for heading in (
            "## Goal",
            "## Before you start",
            "## Steps",
            "## When you are done",
            "## When you get stuck",
        ):
            assert heading in text, f"{guide.parent.name}: {heading}"
        assert "Complete the `starter/` section" not in text
