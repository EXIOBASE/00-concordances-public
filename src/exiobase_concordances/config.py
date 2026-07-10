"""Path to the published concordance tables.

"""

from __future__ import annotations

from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CONCORDANCES = REPO_ROOT / "concordances"
