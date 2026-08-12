from __future__ import annotations

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate(path: Path = ROOT / "curriculum/curriculum.yml") -> list[str]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    weeks = data.get("weeks", [])
    errors: list[str] = []
    ids = [week.get("id") for week in weeks]
    if ids != list(range(1, 25)):
        errors.append("weeks must contain ordered ids 1..24")
    milestones = [(week.get("id"), week.get("milestone")) for week in weeks if week.get("milestone")]
    expected_milestones = [(week, f"milestone-{index:02d}") for index, week in enumerate(range(4, 25, 4), 1)]
    if milestones != expected_milestones:
        errors.append("cần đúng sáu mốc năng lực theo thứ tự ở tuần 4, 8, 12, 16, 20, 24")
    for week in weeks:
        hours = week.get("hours")
        if not isinstance(hours, int) or not 8 <= hours <= 10:
            errors.append(f"week {week.get('id')} workload must be 8-10 hours")
        environments = set(week.get("environments", []))
        if "aws" in environments and week.get("id", 0) < 21:
            errors.append(f"week {week.get('id')} cannot require AWS")
        if week.get("cost_class") == "free-compute" and not environments & {"colab", "kaggle"}:
            errors.append(f"week {week.get('id')} needs a free compute environment")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print("CURRICULUM FAIL")
        for error in errors:
            print(f"- {error}")
        return 1
    print("CURRICULUM PASS: 24 weeks; 6 milestones; workload valid; cost staging valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
