# Concordance tables

The published concordances, organised by category:

- `aggregations/` - EXIOBASE detail mapped to coarser groupings
  (7 sectors, consumption categories, ESA59, CC17, CC41r, etc.).
- `exiobase/` - EXIOBASE-internal map (product -> industry).
- `international/` - external classifications -> EXIOBASE (CPA, ISIC, HS,
  NACE, NAICS, COICOP, FAO).
- `nsi_bridges/` - national supply/use bridges, kept as-is (original
  workbooks).

Each concordance is a long CSV (`source_code, source_name, target_code,
target_name, weight`); a wide matrix mirror sits under each category's
`_wide/` folder. Files are named `<source>_<target>.csv` (split on the
first underscore).
