from __future__ import annotations

import json
from pathlib import Path


def select_profile(cuda_available: bool) -> str:
    return "gpu-free" if cuda_available else "cpu-mini"


def checkpoint_state(path: Path, epoch: int, history: list[float], seed: int) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps({"epoch": epoch, "history": history, "seed": seed}, indent=2),
        encoding="utf-8",
    )

