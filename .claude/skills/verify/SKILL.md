---
name: verify
description: Run a verification checklist over the current state of the yard waste fee / budget analysis in this project — data sourced, math checked, claims traceable, gaps disclosed. Use when the user says "/verify", asks "did we check everything?", or before delivering a final conclusion or report.
---

# Verify

A pre-delivery checklist for this project's budget/fee analysis. Don't just assert "looks good" — walk each item and report status.

## Checklist

1. **Source grounding**: every number in the analysis traces to a specific page/table in the source PDF (or another named document) — not inferred or estimated without saying so.
2. **Math re-derived**: percentages, totals, and ratios were recomputed independently (see the `spot-check` skill), not just copied from the PDF's own printed % change column.
3. **Missing data disclosed**: if the actual yard waste cart fee / pickup fee schedule still hasn't been located, that gap is stated up front in any report — never implied to be answered.
4. **Scope match**: conclusions about "yard waste" specifically aren't silently drawn from "Solid Waste" totals (which include trash + recycling + yard waste combined) without flagging that the figures are for the whole division, not yard waste alone.
5. **Anomalies explained or flagged**: any outlier (e.g. a division jumping 100%+) either has a cited explanation from the source text or is explicitly called out as unexplained.
6. **Comparisons apples-to-apples**: year-over-year comparisons use consistent basis (e.g. "Recommended" vs prior year "Original Budget", not vs "Estimated" actuals, unless labeled).

## Output

Go through each item, mark it done / not applicable / still open, and for anything open, say exactly what's missing and what would resolve it.
