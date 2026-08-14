import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


@pytest.mark.skipif(shutil.which("pwsh") is None, reason="PowerShell is not installed")
def test_powershell_release_gate_fails_fast_on_first_validator_error(tmp_path: Path) -> None:
    scripts = tmp_path / "scripts"
    scripts.mkdir()
    (scripts / "check.ps1").write_bytes((ROOT / "scripts/check.ps1").read_bytes())
    result = subprocess.run(
        ["pwsh", "-NoProfile", "-File", str(scripts / "check.ps1"), "-Scope", "all", "-Profile", "release"],
        cwd=tmp_path,
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    output = result.stdout + result.stderr
    assert "validate_curriculum.py" in output
    assert "validate_sources.py" not in output
