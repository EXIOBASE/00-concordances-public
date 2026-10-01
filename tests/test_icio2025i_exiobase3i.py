"""Pin the OECD ICIO 2025 -> EXIOBASE industry concordance on the rows that
have been wrong before, and check the wide mirror against the long table.

Run from the repository root with ``python -m pytest tests``.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from exiobase_concordances import loaders, schema  # noqa: E402

CONCORDANCES = ROOT / "concordances"
NAME = "icio2025i_exiobase3i"


def _targets(long: pd.DataFrame, source_code: str) -> set[str]:
    return set(long.loc[long["source_code"] == source_code, "target_code"])


def test_c28_is_machinery_manufacturing_only():
    long = loaders.load("international", NAME, CONCORDANCES)
    assert _targets(long, "C28") == {"i29"}


def test_n_carries_renting_and_other_business_activities():
    long = loaders.load("international", NAME, CONCORDANCES)
    assert _targets(long, "N") == {"i71", "i74"}


def test_i71_has_exactly_one_icio_source():
    long = loaders.load("international", NAME, CONCORDANCES)
    assert set(long.loc[long["target_code"] == "i71", "source_code"]) == {"N"}


def test_wide_mirror_matches_long():
    long = loaders.load("international", NAME, CONCORDANCES)
    wide = loaders.load_wide("international", NAME, CONCORDANCES)
    assert schema.wide_to_pairs(wide) == schema.long_to_pairs(schema.tidy_long(long))
