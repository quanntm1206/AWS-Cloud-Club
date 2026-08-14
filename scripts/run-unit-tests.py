"""Run the complete repository test suite with one cross-platform command."""

from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    sys.path.insert(0, str(root))

    import pytest

    return pytest.main(["-q"])

if __name__ == "__main__":
    raise SystemExit(main())
