from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def _field(text: str, label: str) -> str:
    marker = f"**{label}:**"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].splitlines()[0].strip()


def _listed_terms(value: str) -> list[str]:
    return [part for index, part in enumerate(value.split("`")) if index % 2 == 1]


def validate(root: Path = ROOT, *, require_complete: bool = True) -> list[str]:
    errors: list[str] = []
    week_paths = sorted((root / "roadmap/weeks").glob("week-*.md"))
    lab_paths = sorted((root / "labs").glob("lab-[0-9][0-9]-*/README.md"))
    glossary_path = root / "curriculum/glossary.yml"

    if require_complete and len(week_paths) != 24:
        errors.append(f"expected 24 week guides, found {len(week_paths)}")
    if require_complete and len(lab_paths) != 21:
        errors.append(f"expected 21 lab guides, found {len(lab_paths)}")

    for path in week_paths:
        text = path.read_text(encoding="utf-8")
        for heading in (
            "## Why this week matters",
            "## Keywords for this week",
            "## Signs that you understand",
            "## When you get stuck",
        ):
            if heading not in text:
                errors.append(f"{path.relative_to(root)} missing {heading}")
        if "## Keywords for this week" in text:
            vocabulary = text.split("## Keywords for this week", 1)[1].split("##", 1)[0]
            for label in ("**Review:**", "**Use:**"):
                if label not in vocabulary:
                    errors.append(f"{path.relative_to(root)} vocabulary missing {label}")

        hours = []
        for line in text.splitlines():
            if line.startswith("|") and line.count("|") >= 3:
                value = line.split("|")[-2].strip()
                if value.isdigit():
                    hours.append(int(value))
        if not 8 <= sum(hours) <= 10:
            errors.append(f"{path.relative_to(root)} schedule totals {sum(hours)} hours")

    term_specs: dict[str, dict[str, object]] = {}
    if not glossary_path.exists():
        errors.append("curriculum/glossary.yml missing")
    else:
        glossary = yaml.safe_load(glossary_path.read_text(encoding="utf-8")) or {}
        terms = glossary.get("terms", [])
        if require_complete and len(terms) < 50:
            errors.append(f"glossary needs at least 50 terms, found {len(terms)}")
        for index, item in enumerate(terms):
            if not isinstance(item, dict):
                errors.append(f"glossary term {index} must be a mapping")
                continue
            missing = {"term", "meaning", "example", "introduced_in"} - item.keys()
            if missing:
                errors.append(f"glossary term {index} missing {sorted(missing)}")
                continue
            term = str(item["term"])
            if term in term_specs:
                errors.append(f"duplicate glossary term {term}")
            if not isinstance(item["introduced_in"], int) or not 0 <= item["introduced_in"] <= 20:
                errors.append(f"glossary term {term} has invalid introduced_in")
            if not str(item["meaning"]).strip() or not str(item["example"]).strip():
                errors.append(f"glossary term {term} needs meaning and example")
            term_specs[term] = item

    for path in lab_paths:
        text = path.read_text(encoding="utf-8")
        lab_number = int(path.parent.name.split("-")[1])
        for heading in (
            "## Terms used in this lab",
        ):
            if heading not in text:
                errors.append(f"{path.relative_to(root)} missing {heading}")
        if "Complete the `starter/` section" in text:
            errors.append(f"{path.relative_to(root)} presents the smoke starter as an unfinished exercise")

        new_value = _field(text, "New terms")
        review_value = _field(text, "Review")
        application = _field(text, "Use in this lab")
        self_explain = _field(text, "Explain it yourself")
        new_terms = _listed_terms(new_value)
        review_terms = _listed_terms(review_value)
        if not new_terms:
            errors.append(f"{path.relative_to(root)} needs new terms")
        if not application or not self_explain:
            errors.append(f"{path.relative_to(root)} needs application and self-explanation")
        if lab_number == 0:
            if not review_value.lower().startswith("none"):
                errors.append(f"{path.relative_to(root)} lab 00 review must say None")
        elif len(review_terms) < 2:
            errors.append(f"{path.relative_to(root)} needs at least two prior review terms")

        for term in new_terms:
            spec = term_specs.get(term)
            if spec is None:
                errors.append(f"{path.relative_to(root)} unknown new term {term}")
                continue
            introduced_in = int(spec["introduced_in"])
            if introduced_in > lab_number:
                errors.append(f"{path.relative_to(root)} term {term} introduced in a future lab")
            elif introduced_in < lab_number:
                errors.append(f"{path.relative_to(root)} term {term} should be review, not new")
            if term.lower() not in application.lower():
                errors.append(f"{path.relative_to(root)} application must use term {term}")

        for term in review_terms:
            spec = term_specs.get(term)
            if spec is None:
                errors.append(f"{path.relative_to(root)} unknown review term {term}")
                continue
            if int(spec["introduced_in"]) >= lab_number:
                errors.append(f"{path.relative_to(root)} review term {term} is not from a prior lab")
            normalized_term = term.lower().replace(" / ", " ")
            combined = f"{application} {self_explain}".lower().replace(" / ", " ")
            if normalized_term not in combined:
                errors.append(f"{path.relative_to(root)} must apply or explain review term {term}")

        expected_path = path.parent / "expected/README.md"
        if not expected_path.exists() or "## Terminology oracle" not in expected_path.read_text(encoding="utf-8"):
            errors.append(f"{path.relative_to(root)} expected receipt missing terminology oracle")

    for term, spec in term_specs.items():
        introduced_in = int(spec["introduced_in"])
        matching = [path for path in lab_paths if int(path.parent.name.split("-")[1]) == introduced_in]
        if matching and f"`{term}`" not in matching[0].read_text(encoding="utf-8"):
            errors.append(f"glossary term {term} missing from its introduction lab {introduced_in}")

        for path in lab_paths:
            lab_number = int(path.parent.name.split("-")[1])
            if lab_number < introduced_in and re.search(
                rf"(?<![\w-])`{re.escape(term)}`(?![\w-])", path.read_text(encoding="utf-8"), re.IGNORECASE
            ):
                errors.append(f"{path.relative_to(root)} uses term {term} before lab {introduced_in}")
        # Week guides preview terms before the matching lab; validate only explicit
        # glossary tokens, not ordinary English prose that happens to contain a term.
        for path in week_paths:
            week_number = int(path.stem.split("-")[1])
            equivalent_lab = min(week_number - 1, 20)
            if equivalent_lab < introduced_in and re.search(
                rf"(?<![\w-])`{re.escape(term)}`(?![\w-])", path.read_text(encoding="utf-8"), re.IGNORECASE
            ):
                errors.append(f"{path.relative_to(root)} uses term {term} before lab {introduced_in}")

    return errors


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    errors = validate()
    if errors:
        print("LEARNER DOCS FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("LEARNER DOCS PASS: 24 weeks; 21 labs; mentor guidance, spiral vocabulary and workload valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
