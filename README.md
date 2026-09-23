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
