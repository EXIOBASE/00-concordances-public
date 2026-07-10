"""Canonical concordance schema and the long <-> wide round-trip.

A concordance is stored in two views that must encode the same mapping:

* **long** - the source of truth. One row per mapped pair, columns
  ``source_code, source_name, target_code, target_name, weight``. A pair
  is present only if it maps (no explicit zeros). ``weight`` is 1 for a
  plain membership/crosswalk; fractional weights are allowed for splits.
* **wide** - a human-friendly matrix mirror: rows are the source
  identifier, columns the target identifier, cells the weight (0 where
  absent). Built from the long form and checked against it in the tests.

Each axis carries a code and a name. The *identifier* used in the wide
matrix is the code when present, otherwise the name.
"""

from __future__ import annotations

import pandas as pd

LONG_COLUMNS = ["source_code", "source_name", "target_code", "target_name", "weight"]


def _identifier(code: pd.Series, name: pd.Series) -> pd.Series:
    """Code where non-empty, else name. Used as the wide-matrix axis label."""
    code = code.fillna("").astype(str).str.strip()
    name = name.fillna("").astype(str).str.strip()
    return code.where(code != "", name)


def tidy_long(df: pd.DataFrame) -> pd.DataFrame:
    """Return ``df`` with the canonical column set and order, validated.

    Enforces the concordance invariants: every pair has a non-empty source
    and target identifier, no zero weights, and no duplicate
    ``(source, target)`` pairs (a mapping is a set of weighted pairs).
    """
    missing = [c for c in LONG_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"long frame missing columns: {missing}")
    out = df[LONG_COLUMNS].copy()
    for c in ("source_code", "source_name", "target_code", "target_name"):
        out[c] = out[c].fillna("").astype(str).str.strip()
    out["weight"] = pd.to_numeric(out["weight"], errors="raise")
    out = out[out["weight"] != 0]

    s_id = _identifier(out["source_code"], out["source_name"])
    t_id = _identifier(out["target_code"], out["target_name"])
    out = out[(s_id != "") & (t_id != "")]
    out = out[~pd.concat([s_id, t_id], axis=1).loc[out.index].duplicated()]
    return out.reset_index(drop=True)


def long_to_wide(long_df: pd.DataFrame) -> pd.DataFrame:
    """Build the wide matrix mirror from a long concordance.

    Rows and columns preserve first-appearance order from the long frame.
    """
    df = long_df.copy()
    df["_s"] = _identifier(df["source_code"], df["source_name"])
    df["_t"] = _identifier(df["target_code"], df["target_name"])
    row_order = list(dict.fromkeys(df["_s"]))
    col_order = list(dict.fromkeys(df["_t"]))
    wide = (
        df.pivot_table(index="_s", columns="_t", values="weight", aggfunc="sum", fill_value=0)
        .reindex(index=row_order, columns=col_order, fill_value=0)
    )
    wide.index.name = "source"
    wide.columns.name = None
    return wide


def wide_to_pairs(wide_df: pd.DataFrame) -> set[tuple[str, str, float]]:
    """Melt a wide matrix to the set of non-zero ``(source, target, weight)``."""
    src = wide_df.index.name or "index"
    m = wide_df.copy().reset_index().melt(id_vars=src, var_name="target", value_name="weight")
    m = m[m["weight"] != 0]
    return {(str(r[src]), str(r["target"]), float(r["weight"])) for _, r in m.iterrows()}


def long_to_pairs(long_df: pd.DataFrame) -> set[tuple[str, str, float]]:
    """The ``(source, target, weight)`` set implied by a long concordance."""
    df = long_df.copy()
    s = _identifier(df["source_code"], df["source_name"])
    t = _identifier(df["target_code"], df["target_name"])
    return {(a, b, float(w)) for a, b, w in zip(s, t, df["weight"])}
