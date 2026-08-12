from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from pathlib import Path


def export_artifacts(source: Path, output: Path) -> dict[str, object]:
    required = ["metrics.json", "manifest.json", "model-card.md"]
    missing = [name for name in required if not (source / name).exists()]
    if missing:
        raise FileNotFoundError(f"missing required artifacts: {missing}")
    files = sorted(path for path in source.rglob("*") if path.is_file())
    checksums = {
        str(path.relative_to(source)).replace("\\", "/"): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in files
    }
    (source / "export-checksums.json").write_text(
        json.dumps(checksums, indent=2), encoding="utf-8"
    )
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(source.rglob("*")):
            if path.is_file():
                archive.write(path, path.relative_to(source))
    return {"files": len(checksums) + 1, "bytes": output.stat().st_size, "output": str(output)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Package notebook artifacts for durable download")
    parser.add_argument("--source", type=Path, default=Path("artifacts"))
    parser.add_argument("--output", type=Path, default=Path("artifacts.zip"))
    args = parser.parse_args()
    print(export_artifacts(args.source, args.output))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

