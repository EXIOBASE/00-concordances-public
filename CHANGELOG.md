# Changelog

All notable changes to the published tables are recorded here. Format
follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). Write
entries from the consumer's perspective (what changed for someone using a
table), newest first.

## [Unreleased]

### Added

- `international/faoisscaap_exiobase3p` (45 rows): FAO ISSCAAP fishery
  groups -> `p05`. Fishery was not previously covered by any table.
- `international/faoitem_cpa2002` (184 rows): FAO production items ->
  CPA 2002 at 6-digit, for the crop and forestry items. Some CPA classes
  are coarser than the FAO item, so chaining FAO -> CPA -> EXIOBASE does
  not always reproduce `fao_exiobase3p`; prefer the direct table.
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

### Changed

- `international/fao_exiobase3p` now carries **FAO item codes**: 237 of
  its 263 rows have one, matched by exact item name against the FAO item
  lists used by the EXIOBASE FAO extensions. The 26 rows with no
  unambiguous code keep an empty `source_code` and are still identified
  by name; no codes were guessed. Because the wide mirror is keyed on
  code-where-present, its row labels change from item names to item
  codes for the coded rows.
- `international/fao_exiobase3p` lost 31 duplicate rows (294 -> 263).
  Each was a punctuation variant of another row (`Grain mixed` vs
  `Grain, mixed`) mapping to the same product, and one had a
  mojibake-corrupted name. No mapping changed: the set of (item,
  product) pairs is identical before and after.
