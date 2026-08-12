from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    week_paths = sorted((root / "roadmap/weeks").glob("week-*.md"))
    lab_paths = sorted((root / "labs").glob("lab-[0-9][0-9]-*/README.md"))

    if len(week_paths) != 24:
        errors.append(f"expected 24 week guides, found {len(week_paths)}")
    if len(lab_paths) != 21:
        errors.append(f"expected 21 lab guides, found {len(lab_paths)}")

    for path in week_paths:
        text = path.read_text(encoding="utf-8")
        for heading in (
            "## Vì sao tuần này quan trọng",
            "## Dấu hiệu bạn đã hiểu",
            "## Khi mắc kẹt",
        ):
            if heading not in text:
                errors.append(f"{path.relative_to(root)} missing {heading}")

        hours = []
        for line in text.splitlines():
            if line.startswith("|") and line.count("|") >= 3:
                value = line.split("|")[-2].strip()
                if value.isdigit():
                    hours.append(int(value))
        if not 8 <= sum(hours) <= 10:
            errors.append(f"{path.relative_to(root)} schedule totals {sum(hours)} hours")

    for path in lab_paths[:20]:
        text = path.read_text(encoding="utf-8")
        for heading in (
            "## Mục tiêu",
            "## Trước khi bắt đầu",
            "## Các bước thực hiện",
            "## Khi nào xem như hoàn thành",
            "## Khi mắc kẹt",
        ):
            if heading not in text:
                errors.append(f"{path.relative_to(root)} missing {heading}")
        if "Hoàn thiện phần `starter/`" in text:
            errors.append(f"{path.relative_to(root)} presents the smoke starter as an unfinished exercise")

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
    print("LEARNER DOCS PASS: 24 weeks; 21 labs; mentor guidance and workload valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
