import json
from pathlib import Path

from scripts.export_notebook import export_artifacts


def test_export_artifacts_creates_checksummed_zip(tmp_path: Path) -> None:
    source = tmp_path / "artifacts"
    source.mkdir()
    (source / "metrics.json").write_text(json.dumps({"macro_f1": 0.7}), encoding="utf-8")
    (source / "manifest.json").write_text(json.dumps({"seed": 42}), encoding="utf-8")
    (source / "model-card.md").write_text("# Model card", encoding="utf-8")
    output = tmp_path / "artifacts.zip"
    result = export_artifacts(source, output)
    assert output.exists()
    assert result["files"] == 4

