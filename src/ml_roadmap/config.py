from __future__ import annotations

from dataclasses import dataclass, fields
from pathlib import Path

import yaml


@dataclass(frozen=True)
class TrainConfig:
    target: str
    seed: int = 42
    test_size: float = 0.2
    validation_size: float = 0.2
    threshold: float = 0.5
    tune_threshold: bool = True

    def __post_init__(self) -> None:
        if not self.target.strip():
            raise ValueError("target cannot be empty")
        if not 0 < self.test_size < 1:
            raise ValueError("test_size must be between 0 and 1")
        if not 0 < self.validation_size < 1 or self.test_size + self.validation_size >= 1:
            raise ValueError("validation_size must be positive and leave training data")
        if not 0 <= self.threshold <= 1:
            raise ValueError("threshold must be between 0 and 1")


def load_config(path: Path) -> TrainConfig:
    values = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(values, dict):
        raise ValueError("config must be a mapping")
    allowed = {field.name for field in fields(TrainConfig)}
    unknown = set(values) - allowed
    if unknown:
        raise ValueError(f"unknown config keys: {sorted(unknown)}")
    return TrainConfig(**values)
