---
name: data-quality
description: Check a dataset extracted from this project's budget PDF (or any CSV/Excel here) for nulls, duplicates, outliers, and row loss versus the source. Use when the user says "/data-quality", asks to validate extracted numbers, worries data was "extracted wrong," or before doing analysis on any table pulled out of the PDF.
---

# Data Quality Check

Before trusting any table pulled from `fy2026-27-managers-recommended-budget.pdf` (or elsewhere), verify it wasn't mangled in extraction — PDF table extraction commonly drops rows, merges columns, or turns `$` figures into garbage strings.

## Checks to run

1. **Row count vs source**: re-extract the relevant page(s) independently (e.g. with `pdfplumber`'s `extract_tables()` or a second look at `pypdf` text) and confirm the row count matches. Flag any missing division/line-item.
2. **Nulls**: report which columns/rows have missing values, and whether that's expected (e.g. "N/A" for a fund with no prior-year comparison) or a sign of a dropped cell.
3. **Duplicates**: check for duplicate rows (same division/line-item appearing twice), which usually means a table spanned a page break and got double-counted.
4. **Type sanity**: dollar columns should parse to numeric after stripping `$` and `,`; percent columns should be in a sane range (roughly -100% to +300% for a single year change — anything wilder is worth a second look, not necessarily wrong).
5. **Outliers**: flag values far outside the pattern of the rest of the column (e.g. a division jumping 200%+ or dropping to $0) and check the PDF narrative text on that page — it usually explains the anomaly (e.g. "no longer leasing the Mallette parking lot" for the 100% drop in Mallette Lot revenue). Don't just flag it — say whether the source text explains it or not.
6. **Totals check**: where the source has a "Total" row, sum the components and confirm it matches — this is the single best signal that extraction didn't drop or duplicate a row.

## Output

A short report: pass/fail per check, and for anything flagged, the specific row/value plus either the explanation found in the source PDF or a note that it needs the user's attention.
