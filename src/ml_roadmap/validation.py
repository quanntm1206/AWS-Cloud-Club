from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import pandas as pd


@dataclass(frozen=True)
class DataSchema:
    required: tuple[str, ...]
    allow_extra: bool = False


@dataclass(frozen=True)
class ValidationReport:
    missing: tuple[str, ...]
    extra: tuple[str, ...]

    @property
    def valid(self) -> bool:
        return not self.missing and not self.extra


def validate_frame(frame: pd.DataFrame, schema: DataSchema) -> ValidationReport:
    columns = set(frame.columns)
    required = set(schema.required)
    missing = tuple(sorted(required - columns))
    extra = () if schema.allow_extra else tuple(sorted(columns - required))
    return ValidationReport(missing=missing, extra=extra)


def main() -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Validate a CSV against required columns")
    parser.add_argument("csv", type=Path)
    parser.add_argument("--required", nargs="+", required=True)
    args = parser.parse_args()
    report = validate_frame(pd.read_csv(args.csv), DataSchema(tuple(args.required)))
    print(report)
    return 0 if report.valid else 1

