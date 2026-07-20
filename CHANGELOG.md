# Changelog

All notable changes to the published tables are recorded here. Format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Write
entries from the consumer's perspective (what changed for someone using a
table), newest first.

## [Unreleased]

### Added

- Github repo of EXIOBASE concordance tables. 
- Published concordances, each as a long CSV plus a `_wide/` matrix mirror:
  - `aggregations/` (9): EXIOBASE detail -> 7 sectors, 7 consumption
    categories (+ a detailed breakdown), ESA59, CC17, CC41r regions,
    EXIOBASE1.0 products.
  - `exiobase/` (1): product -> industry.
  - `international/` (11): CPA 2002, CPA SUT 64 (Eurostat A64), ISIC
    Rev.3, HS 1996, NACE Rev.2 (two variants), NAICS 2017, COICOP
    (-> product and -> ISIC), FAO production items, and OECD ICIO 2025
    industries, all mapped to EXIOBASE.
  - `nsi_bridges/`: national supply/use bridges (original workbooks).
- Small read-only Python loader (`exiobase_concordances`): `load`,
  `load_wide`, `list_concordances`, `has_wide`. Requires only `pandas`.
