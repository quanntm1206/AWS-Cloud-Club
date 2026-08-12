from __future__ import annotations

import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


class CloudFormationLoader(yaml.SafeLoader):
    pass


def _construct_tag(loader: CloudFormationLoader, tag_suffix: str, node: yaml.Node) -> object:
    del tag_suffix
    if isinstance(node, yaml.ScalarNode):
        return loader.construct_scalar(node)
    if isinstance(node, yaml.SequenceNode):
        return loader.construct_sequence(node)
    return loader.construct_mapping(node)


CloudFormationLoader.add_multi_constructor("!", _construct_tag)


def validate_aws(root: Path = ROOT) -> list[str]:
    policy = yaml.safe_load((root / "aws/cost-policy.yml").read_text(encoding="utf-8"))
    template_text = (root / "aws/cloudformation/tabular-inference.yml").read_text(encoding="utf-8")
    template = yaml.load(template_text, Loader=CloudFormationLoader)
    errors: list[str] = []
    resources = template.get("Resources", {})
    resource_types = {resource.get("Type") for resource in resources.values()}
    forbidden = set(policy["forbidden_resources"])
    unexpected = resource_types & forbidden
    if unexpected:
        errors.append(f"forbidden resources: {sorted(unexpected)}")
    allowed_prefixes = ("AWS::S3::", "AWS::Lambda::", "AWS::Logs::", "AWS::IAM::")
    for name, resource in resources.items():
        resource_type = resource.get("Type", "")
        if not resource_type.startswith(allowed_prefixes):
            errors.append(f"{name}: type not allowlisted: {resource_type}")
    if "PublicAccessBlockConfiguration" not in template_text:
        errors.append("S3 public access block is required")
    if "RetentionInDays: 1" not in template_text:
        errors.append("CloudWatch log retention must be one day")
    if "ReservedConcurrentExecutions: 1" not in template_text:
        errors.append("Lambda reserved concurrency must be one")
    if "AWS::ApiGatewayV2" in template_text or "EnablePublicApi" in template_text:
        errors.append("learner template must use private Lambda invocation only")
    for tag in policy["required_tags"]:
        if not re.search(rf"(?:Key:\s*{re.escape(tag)}\b|^\s*{re.escape(tag)}:)", template_text, re.M):
            errors.append(f"missing required tag: {tag}")
    if re.search(r"Action:\s*['\"]?\*", template_text):
        errors.append("wildcard IAM action is forbidden")
    return errors


def main() -> int:
    errors = validate_aws()
    if errors:
        print("AWS SAFETY FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("AWS SAFETY PASS: allowlist, denylist, tags, retention and concurrency valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
