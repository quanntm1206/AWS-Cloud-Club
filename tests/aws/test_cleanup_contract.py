import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def test_cleanup_scripts_default_to_dry_run_and_scope_stack() -> None:
    for suffix in ("ps1", "sh"):
        text = (ROOT / f"aws/scripts/cleanup.{suffix}").read_text(encoding="utf-8")
        assert "dry-run" in text.lower() or "DryRun" in text
        assert "ml-roadmap-" in text
        assert "delete-stack" in text
        assert "s3 rm" in text
        assert "list-stack-resources" in text


def test_powershell_and_bash_expose_same_lifecycle_scripts() -> None:
    names = {"preflight", "cost-check", "deploy", "cleanup", "residual-scan"}
    assert names == {path.stem for path in (ROOT / "aws/scripts").glob("*.ps1")}
    assert names == {path.stem for path in (ROOT / "aws/scripts").glob("*.sh")}


def test_deploy_calls_preflight_before_cloudformation() -> None:
    for suffix in ("ps1", "sh"):
        text = (ROOT / f"aws/scripts/deploy.{suffix}").read_text(encoding="utf-8")
        assert "preflight" in text
        assert text.index("preflight") < text.index("cloudformation deploy")
        assert "AcknowledgeBudgetConfigured" in text or "acknowledge-budget-configured" in text


def test_residual_scan_covers_every_resource_allowlist_service() -> None:
    for suffix in ("ps1", "sh"):
        text = (ROOT / f"aws/scripts/residual-scan.{suffix}").read_text(encoding="utf-8")
        commands = (
            ("s3api", "list-buckets"),
            ("lambda", "list-functions"),
            ("logs", "describe-log-groups"),
            ("iam", "list-roles"),
            ("apigatewayv2", "get-apis"),
        )
        for service, action in commands:
            assert service in text and action in text
        assert "scan_status" in text
        assert "AWS scan error" in text


@pytest.mark.skipif(sys.platform != "win32", reason="PowerShell PATH/PATHEXT contract is Windows-only")
def test_powershell_residual_scan_fails_closed_on_cli_error(tmp_path: Path) -> None:
    fake_aws = tmp_path / "aws.ps1"
    fake_aws.write_text("[Console]::Error.WriteLine('AccessDenied')\nexit 7\n", encoding="ascii")
    script = ROOT / "aws/scripts/residual-scan.ps1"
    result = subprocess.run(
        [
            "pwsh",
            "-NoProfile",
            "-File",
            str(script),
            "-ProjectId",
            "student01",
        ],
        env={
            "PATH": f"{tmp_path};{Path('C:/Windows/System32')}",
            "PATHEXT": ".PS1;.EXE;.CMD;.BAT",
        },
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode != 0
    assert "AccessDenied" in result.stderr + result.stdout


def test_bash_cleanup_does_not_swallow_aws_failures() -> None:
    text = (ROOT / "aws/scripts/cleanup.sh").read_text(encoding="utf-8")
    assert "|| true" not in text
    assert "--confirm-project-id" in text
    assert "set -euo pipefail" in text
