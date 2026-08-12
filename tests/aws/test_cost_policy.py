import textwrap
from pathlib import Path

import yaml

from scripts.validate_aws_safety import validate_aws

ROOT = Path(__file__).resolve().parents[2]


def test_cost_policy_and_template_pass() -> None:
    assert validate_aws() == []


def test_policy_contains_required_cost_guards() -> None:
    policy = yaml.safe_load((ROOT / "aws/cost-policy.yml").read_text(encoding="utf-8"))
    assert "AWS::EC2::NatGateway" in policy["forbidden_resources"]
    assert "AWS::SageMaker::Endpoint" in policy["forbidden_resources"]
    assert policy["limits"]["lambda_reserved_concurrency"] == 1
    assert "not a hard spending cap" in policy["budget_caveat"]


def test_optional_http_api_is_wired_not_orphaned() -> None:
    text = (ROOT / "aws/cloudformation/tabular-inference.yml").read_text(encoding="utf-8")
    for resource in ("HttpApiIntegration", "HttpApiRoute", "HttpApiStage", "HttpApiPermission"):
        assert resource in text


def test_inline_lambda_uses_index_handler() -> None:
    text = (ROOT / "aws/cloudformation/tabular-inference.yml").read_text(encoding="utf-8")
    assert "Handler: index.lambda_handler" in text
    assert "except json.JSONDecodeError" in text
    assert "body must be an object" in text
    assert '"statusCode": 422' in text
    assert "invalid field type or value" in text
    assert '"statusCode": 503' in text
    assert "model unavailable" in text
    assert "schema_version" in text
    assert "model_sha256" in text
    assert "portable artifact checksum mismatch" in text


def test_powershell_deploy_checks_every_aws_exit_code() -> None:
    text = (ROOT / "aws/scripts/deploy.ps1").read_text(encoding="utf-8")
    assert text.count("aws cloudformation") == 3
    assert text.count("aws s3 cp") == 1
    assert text.count("$LASTEXITCODE -ne 0") == 4
    assert "Stack did not return BucketName" in text


def test_powershell_preflight_and_cleanup_fail_closed() -> None:
    preflight = (ROOT / "aws/scripts/preflight.ps1").read_text(encoding="utf-8")
    cleanup = (ROOT / "aws/scripts/cleanup.ps1").read_text(encoding="utf-8")
    assert "AWS identity lookup failed; preflight stopped" in preflight
    assert preflight.count("$LASTEXITCODE -ne 0") == 1
    assert cleanup.count("$LASTEXITCODE -ne 0") == 5
    assert "-ConfirmProjectId <exact-id>" in cleanup
    assert "Bucket cleanup failed; stack deletion stopped" in cleanup


def test_cost_checks_publish_bounded_assumptions_and_primary_sources() -> None:
    for suffix in ("ps1", "sh"):
        text = (ROOT / f"aws/scripts/cost-check.{suffix}").read_text(encoding="utf-8")
        assert "USD 0.00-0.10" in text
        assert "<=100 Lambda invokes" in text
        assert "assuming no Free Tier/credits" in text
        assert "https://aws.amazon.com/lambda/pricing/" in text
        assert "not a bill guarantee" in text


def test_cloudformation_embeds_the_tested_lambda_handler() -> None:
    template = (ROOT / "aws/cloudformation/tabular-inference.yml").read_text(encoding="utf-8")
    embedded = template.split("        ZipFile: |\n", 1)[1].split("      Environment:\n", 1)[0]
    deployed_handler = textwrap.dedent(embedded).strip()
    tested_handler = (ROOT / "aws/lambda/handler.py").read_text(encoding="utf-8").strip()
    assert deployed_handler == tested_handler
