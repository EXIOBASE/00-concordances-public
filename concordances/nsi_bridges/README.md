# National statistics bridges (as-is)

National supply/use table (SUT) to EXIOBASE bridges, kept in their
**original workbook form** (not reformatted to the long/wide concordance
schema):

- `Bridge_NSI_<country>.xlsx` - one per country, each with supply/use
  bridges for products and industries (sheets `<CC>_c_sup`, `<CC>_r_sup`,
  `<CC>_c_use`, `<CC>_r_use`).
- `EXIOBASE3/` - EXIOBASE3 NACE index workbooks.
- `US/` - USEEIO concordances (Wolfram, Sinha variants).

These are build-internal bridges with country-specific multi-row-header
matrices, preserved here for provenance and reuse. If a normalised long
form is needed for a specific country, convert it on demand.
