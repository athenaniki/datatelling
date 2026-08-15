---
name: spot-check
description: Validate a computed number or claim in this project's budget analysis by tracing it back to the raw source PDF. Use when the user says "/spot-check", asks "is that right?", "where does that number come from?", or before finalizing any conclusion about the yard waste fee rationale or budget analysis.
---

# Spot Check

Pick a specific computed result (a total, a % change, a ratio like cost-per-cart) and verify it against the raw source, independent of however it was originally calculated.

## Steps

1. Identify the claim to check (e.g. "Solid Waste division increased 4.7%").
2. Go back to the primary source — re-read the actual PDF page (not a cached extraction) using the `pdf` skill or `pypdf`/`pdfplumber` directly.
3. Recompute independently: pull the two raw numbers and redo the arithmetic yourself rather than trusting the extracted percentage. For a % change: `(new - old) / old * 100`.
4. Compare: does the recomputed value match the claim within rounding? If not, say exactly where the discrepancy is (wrong page, wrong row, transcription error, or a genuine math error).
5. Report clearly: **confirmed** (matches, cite page/line) or **discrepancy found** (show both values and the likely cause).

Don't spot-check by re-reading the same extracted table you already trust — go back to the PDF page image/text itself, since that's the only way to catch an extraction error.
