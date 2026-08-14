from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
DEEP_GLOSSARY_FIELDS = {"why_it_matters", "common_confusion", "self_check"}


def _field(text: str, label: str) -> str:
    marker = f"**{label}:**"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].splitlines()[0].strip()


def _listed_terms(value: str) -> list[str]:
    return [part for index, part in enumerate(value.split("`")) if index % 2 == 1]


def _section(text: str, heading: str) -> str:
    marker = f"## {heading}"
    if marker not in text:
        return ""
    return text.split(marker, 1)[1].split("\n## ", 1)[0].strip()


def _concept_groups(section: str) -> list[tuple[str, str]]:
    groups: list[tuple[str, str]] = []
    for chunk in re.split(r"(?m)^###\s+", section)[1:]:
        lines = chunk.strip().splitlines()
        if lines:
            groups.append((lines[0].strip(), "\n".join(lines[1:])))
    return groups


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
            vocabulary = _section(text, "Keywords for this week")
            for label in ("**Review:**", "**Use:**"):
                if label not in vocabulary:
                    errors.append(f"{path.relative_to(root)} vocabulary missing {label}")
            if require_complete:
                concept = _section(text, "Concept walkthrough")
                connection = _section(text, "Connect earlier terms")
                for heading, section in (("Concept walkthrough", concept), ("Connect earlier terms", connection)):
                    if not section:
                        errors.append(f"{path.relative_to(root)} missing ## {heading}")
                for label in ("Mental model", "Why it matters", "Worked example", "Easy to confuse", "Check yourself"):
                    if f"**{label}:**" not in concept:
                        errors.append(f"{path.relative_to(root)} concept walkthrough missing {label}")
                for term in _listed_terms(_field(vocabulary, "New or focus terms")):
                    if f"`{term}`" not in concept:
                        errors.append(f"{path.relative_to(root)} concept walkthrough missing focus term {term}")
                for term in _listed_terms(_field(vocabulary, "Review")):
                    if f"`{term}`" not in connection:
                        errors.append(f"{path.relative_to(root)} prior-term connection missing {term}")

                vi_path = root / "docs/docx-vi/roadmap/weeks" / path.name
                if not vi_path.exists():
                    errors.append(f"{vi_path.relative_to(root)} missing")
                else:
                    vi_text = vi_path.read_text(encoding="utf-8")
                    vi_vocabulary = _section(vi_text, "Từ khóa tuần này")
                    vi_concept = _section(vi_text, "Giải thích khái niệm")
                    vi_connection = _section(vi_text, "Kết nối kiến thức cũ")
                    focus_terms = _listed_terms(_field(vocabulary, "New or focus terms"))
                    review_terms = _listed_terms(_field(vocabulary, "Review"))
                    vi_focus_terms = _listed_terms(_field(vi_vocabulary, "Thuật ngữ mới hoặc trọng tâm"))
                    vi_review_terms = _listed_terms(_field(vi_vocabulary, "Ôn lại"))
                    if vi_focus_terms != focus_terms:
                        errors.append(f"{vi_path.relative_to(root)} focus terms differ from English week")
                    if vi_review_terms != review_terms:
                        errors.append(f"{vi_path.relative_to(root)} review terms differ from English week")
                    for label in (
                        "Cách hình dung",
                        "Vì sao quan trọng",
                        "Ví dụ xuyên suốt",
                        "Dễ nhầm với",
                        "Tự kiểm tra",
                    ):
                        if f"**{label}:**" not in vi_concept:
                            errors.append(f"{vi_path.relative_to(root)} concept walkthrough missing {label}")
                    for term in focus_terms:
                        if f"`{term}`" not in vi_concept:
                            errors.append(f"{vi_path.relative_to(root)} concept walkthrough missing focus term {term}")
                    for term in review_terms:
                        if f"`{term}`" not in vi_connection:
                            errors.append(f"{vi_path.relative_to(root)} prior-term connection missing {term}")

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
            if require_complete:
                deep_missing = DEEP_GLOSSARY_FIELDS - item.keys()
                if deep_missing:
                    errors.append(f"glossary term {term} missing {sorted(deep_missing)}")
                elif not str(item["self_check"]).rstrip().endswith("?"):
                    errors.append(f"glossary term {term} self_check must be a question")
            term_specs[term] = item

    seen_evidence: dict[str, Path] = {}
    seen_oracles: dict[str, Path] = {}
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
        if require_complete:
            concept_application = _section(text, "Apply the concepts")
            if not concept_application:
                errors.append(f"{path.relative_to(root)} missing ## Apply the concepts")
            group_terms: list[str] = []
            groups = _concept_groups(concept_application)
            if not groups:
                errors.append(f"{path.relative_to(root)} concept application needs at least one group")
            for title, body in groups:
                for label in (
                    "Terms",
                    "What they mean here",
                    "Where you will see them",
                    "Common mistake",
                    "Evidence to keep",
                    "Explain after the lab",
                ):
                    if not _field(body, label):
                        errors.append(f"{path.relative_to(root)} concept group {title!r} missing {label}")
                group_terms.extend(_listed_terms(_field(body, "Terms")))
                evidence = re.sub(r"\s+", " ", _field(body, "Evidence to keep").strip().casefold())
                if evidence:
                    previous = seen_evidence.get(evidence)
                    if previous is not None:
                        errors.append(
                            f"{path.relative_to(root)} repeats generic evidence from {previous.relative_to(root)}"
                        )
                    seen_evidence[evidence] = path
            if len(group_terms) != len(set(group_terms)):
                errors.append(f"{path.relative_to(root)} assigns a term to multiple concept groups")
            if set(group_terms) != set(new_terms + review_terms):
                errors.append(f"{path.relative_to(root)} concept groups must own every new/review term exactly")
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
        elif require_complete:
            expected_text = expected_path.read_text(encoding="utf-8")
            oracle = _section(expected_text, "Terminology oracle")
            for label in ("Expected reasoning", "Evidence mapping", "Misconception check"):
                if not _field(oracle, label):
                    errors.append(f"{path.relative_to(root)} terminology oracle missing {label}")
            if "status=starter-example-completed" in _field(oracle, "Evidence mapping"):
                errors.append(f"{path.relative_to(root)} treats starter status as completion evidence")
            if (
                "status=starter-example-completed" in expected_text
                and "does **not** mean that you met all acceptance criteria" not in text
            ):
                errors.append(f"{path.relative_to(root)} lacks explicit starter-status completion guard")
            normalized_oracle = re.sub(r"\s+", " ", oracle.strip().casefold())
            previous = seen_oracles.get(normalized_oracle)
            if previous is not None:
                errors.append(f"{path.relative_to(root)} repeats oracle from {previous.relative_to(root)}")
            seen_oracles[normalized_oracle] = path

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
