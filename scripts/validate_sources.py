from __future__ import annotations

from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

ROOT = Path(__file__).resolve().parents[1]


def validate_sources(path: Path = ROOT / "docs/sources.yml") -> list[str]:
    records = yaml.safe_load(path.read_text(encoding="utf-8")).get("sources", [])
    errors: list[str] = []
    ids: set[str] = set()
    for record in records:
        source_id = record.get("id", "<missing>")
        if source_id in ids:
            errors.append(f"duplicate source id: {source_id}")
        ids.add(source_id)
        if urlparse(str(record.get("url", ""))).scheme != "https":
            errors.append(f"{source_id}: URL must use HTTPS")
        if record.get("authority") not in {"primary", "textbook", "peer-reviewed"}:
            errors.append(f"{source_id}: invalid authority")
        if not record.get("supports"):
            errors.append(f"{source_id}: supports cannot be empty")
        try:
            verified = date.fromisoformat(str(record["verified_on"]))
            recheck = date.fromisoformat(str(record["recheck_after"]))
            if recheck <= verified:
                errors.append(f"{source_id}: recheck_after must follow verified_on")
        except (KeyError, ValueError):
            errors.append(f"{source_id}: invalid verification dates")
    return errors


def main() -> int:
    errors = validate_sources()
    if errors:
        print("SOURCES FAIL")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print("SOURCES PASS: primary-source registry structurally valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

