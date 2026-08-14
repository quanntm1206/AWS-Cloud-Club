"""Render the English curriculum glossary as readable Markdown."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "curriculum" / "glossary.yml"
OUTPUT = ROOT / "roadmap" / "glossary.md"
FIELDS = (
    "term",
    "meaning",
    "why_it_matters",
    "example",
    "common_confusion",
    "self_check",
    "introduced_in",
)


def load_terms() -> list[dict[str, object]]:
    data = yaml.safe_load(SOURCE.read_text(encoding="utf-8"))
    terms = data.get("terms") if isinstance(data, dict) else None
    if not isinstance(terms, list):
        raise ValueError(f"{SOURCE} must contain a 'terms' list")
    for index, item in enumerate(terms):
        if not isinstance(item, dict):
            raise ValueError(f"Term {index} must be a mapping")
        missing = [field for field in FIELDS if field not in item]
        if missing:
            raise ValueError(f"Term {index} is missing: {', '.join(missing)}")
    return terms


def render(terms: list[dict[str, object]]) -> str:
    lines = [
        "# Machine Learning Glossary",
        "",
        "Beginner-friendly definitions, examples, misconceptions, and review questions, "
        "grouped by the lab where each term first appears.",
    ]
    current_lab: object = None
    for item in terms:
        lab = item["introduced_in"]
        if lab != current_lab:
            lines.extend(["", "---", "", f"**Introduced in Lab {int(lab):02d}**"])
            current_lab = lab
        lines.extend(
            [
                "",
                f"## `{item['term']}`",
                "",
                f"**Meaning:** {item['meaning']}",
                "",
                f"**Why it matters:** {item['why_it_matters']}",
                "",
                f"**Example:** {item['example']}",
                "",
                f"**Common confusion:** {item['common_confusion']}",
                "",
                f"**Self-check:** {item['self_check']}",
                "",
                f"**Introduced in:** Lab {int(lab):02d}",
            ]
        )
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="fail if roadmap/glossary.md differs from the generated content",
    )
    args = parser.parse_args()

    expected = render(load_terms())
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print(f"{OUTPUT} is out of date; run {Path(__file__).name}", file=sys.stderr)
            return 1
        return 0

    OUTPUT.write_text(expected, encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
