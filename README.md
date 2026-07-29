# exiobase-concordances

Concordance (correspondence) tables for EXIOBASE classifications:
mappings from EXIOBASE products/industries to ISIC, NACE, HS, CPA, COICOP,
NAICS, and related systems, plus EXIOBASE aggregations and national bridges.


## Layout

```
concordances/
  aggregations/     EXIOBASE detail -> coarser groupings (7 sectors, ESA59, ...)
  exiobase/         EXIOBASE product <-> industry
  international/    external classifications <-> EXIOBASE (CPA, ISIC, HS, ...)
  nsi_bridges/      national supply/use bridges (original workbooks)
  <dir>/_wide/      wide-matrix mirror of each long table
src/exiobase_concordances/   small read-only Python loader (optional)
```

## File format

Each concordance is a tidy long-format CSV, one row per mapped pair, UTF-8:

```
source_code, source_name, target_code, target_name, weight
```

A wide-matrix mirror is provided alongside under `_wide/`. Files are named
`<source>_<target>.csv` (split on the first underscore).

## The FAO tables

| File | Maps |
| --- | --- |
| `fao_exiobase3p` | FAO production items -> EXIOBASE product |
| `faoisscaap_exiobase3p` | FAO ISSCAAP fishery groups -> EXIOBASE product |
| `faoitem_cpa2002` | FAO production items -> CPA 2002 (6-digit) |

`fao_exiobase3p` classifies an FAO commodity as the EXIOBASE product it
*is*, so meat items land in the meat products (`Meat, cattle` ->
`p15.a`) and eggs in `p01.m`. Roughly 90% of its rows carry an FAO item
code; the rest are matched by name only, because the source table
identifies items by name and a few names have no unambiguous code.

Every ISSCAAP group maps to `p05`, since EXIOBASE has a single primary
fishery product. Fishery is kept separate because ISSCAAP is a distinct
code system from FAO item codes.

`faoitem_cpa2002` covers the crop and forestry items only (183 items),
because the livestock and processed-product source lists carry no CPA
codes. Note that going FAO -> CPA -> EXIOBASE does not always reproduce
`fao_exiobase3p`: some CPA classes are coarser than the FAO item. Shea
nuts, for example, sit in CPA `01.13.24` "Olives and other nuts", which
maps to `p01.d`, while both FAO tables place the item in `p01.e` Oil
seeds. Prefer the direct FAO -> EXIOBASE table where the two disagree.

**What is deliberately not here.** The EXIOBASE FAO-based extensions use
a second, different correspondence that sends livestock items back to
the live-animal sector (`Meat, cattle` -> `p01.i`, eggs -> `p01.k`) and
splits fodder crops across five livestock sectors. That is a
fodder-cropland *allocation key* for the land and emission extensions,
not a product classification, so it is not published here. Do not
substitute one for the other: use the extension key only for attributing
FAO production and its environmental pressures to a producing sector.

## Using the tables

The CSVs are self-contained; read them with any tool. A small optional
loader is provided:

```
pip install -e .
```

```python
from exiobase_concordances import list_concordances, load, load_wide

load("international", "hs1996_exiobase3p")   # long form
load_wide("international", "hs1996_exiobase3p")  # wide matrix
```

The loader needs only `pandas`.
