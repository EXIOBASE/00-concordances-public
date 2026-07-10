"""Read published concordance tables.

The long CSV under ``concordances/<category>/<name>.csv`` is the source of
truth; the wide mirror under ``_wide/`` is a view. ``list_concordances``
enumerates everything; ``load`` returns the long form; ``load_wide``
returns the matrix mirror when one exists.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

from . import config


def list_concordances(root: Path | None = None) -> list[tuple[str, str]]:
    """Return ``(category, name)`` for every long concordance CSV."""
    root = root or config.CONCORDANCES
    out: list[tuple[str, str]] = []
    for cat_dir in sorted(p for p in root.iterdir() if p.is_dir()):
        for csv in sorted(cat_dir.glob("*.csv")):
            out.append((cat_dir.name, csv.stem))
    return out


def load(category: str, name: str, root: Path | None = None) -> pd.DataFrame:
    """Load a concordance's long form."""
    root = root or config.CONCORDANCES
    return pd.read_csv(root / category / f"{name}.csv", dtype=str).fillna("").assign(
        weight=lambda d: pd.to_numeric(d["weight"])
    )


def load_wide(category: str, name: str, root: Path | None = None) -> pd.DataFrame:
    """Load a concordance's wide mirror (raises if there is none).

    The index (source identifier) is kept as a string so codes with leading
    zeros (e.g. HS ``010111``) are not silently reparsed as integers; only
    the weight cells are coerced to numeric.
    """
    root = root or config.CONCORDANCES
    wide = pd.read_csv(root / category / "_wide" / f"{name}.csv", index_col=0, dtype=str)
    return wide.apply(pd.to_numeric)


def has_wide(category: str, name: str, root: Path | None = None) -> bool:
    root = root or config.CONCORDANCES
    return (root / category / "_wide" / f"{name}.csv").exists()
