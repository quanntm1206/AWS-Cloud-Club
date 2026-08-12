from pathlib import Path


WORKFLOW_DIR = Path(".github/workflows")
DEPLOY_COMMAND = "aws" + " cloudformation deploy"


def main() -> None:
    violations = []
    for path in WORKFLOW_DIR.glob("*.y*ml"):
        if DEPLOY_COMMAND in path.read_text(encoding="utf-8"):
            violations.append(str(path))
    if violations:
        raise SystemExit(f"CI SAFETY FAIL: deployment command found in {', '.join(violations)}")
    print("CI SAFETY PASS: no AWS deployment command in workflows")


if __name__ == "__main__":
    main()
