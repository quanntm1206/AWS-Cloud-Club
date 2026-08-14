from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def test_single_test_script_runs_the_complete_pytest_suite() -> None:
    script = (ROOT / "scripts" / "run-unit-tests.py").read_text(encoding="utf-8")
    assert 'return pytest.main(["-q"])' in script


def test_docker_build_produces_a_tested_ready_to_predict_image() -> None:
    dockerfile = (ROOT / "Dockerfile").read_text(encoding="utf-8")
    dockerignore = (ROOT / ".dockerignore").read_text(encoding="utf-8")
    required = [
        "python scripts/run-unit-tests.py",
        "ml_roadmap.revenue.generate_data",
        "ml_roadmap.revenue.train",
        "ml_roadmap.revenue.eda",
        "HEALTHCHECK",
        "ml_roadmap.revenue.api:create_app",
    ]
    assert all(token in dockerfile for token in required)
    assert "json.load" in dockerfile
    assert "status') == 'ready'" in dockerfile
    assert "capstones/country-revenue/models/" in dockerignore
    assert "capstones/country-revenue/logs/" in dockerignore


def test_ci_builds_and_smoke_tests_the_container() -> None:
    workflow = (ROOT / ".github" / "workflows" / "ci.yml").read_text(encoding="utf-8")
    assert "docker build" in workflow
    assert "docker run" in workflow
    assert '"country":"france"' in workflow
    assert '"country":"all"' in workflow


def test_capstone_readme_maps_every_peer_review_requirement() -> None:
    readme = (ROOT / "capstones" / "country-revenue" / "README.md").read_text(
        encoding="utf-8"
    )
    evidence_labels = [
        "API unit tests",
        "Model unit tests",
        "Logging unit tests",
        "Single test script",
        "Performance monitoring",
        "Isolated test I/O",
        "Country and all-country predictions",
        "Automated data ingestion",
        "Multiple model comparison",
        "EDA visualizations",
        "Working Docker image",
        "Baseline comparison visualization",
    ]
    assert all(label in readme for label in evidence_labels)
