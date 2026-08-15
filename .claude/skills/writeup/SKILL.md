---
name: writeup
description: Generate a written report from this project's yard waste fee / budget analysis, pulling together data sources, findings, and open questions into a shareable document. Use when the user says "/writeup", asks for a "summary report," "memo," or wants the analysis packaged into something they can send or reference later.
---

# Writeup

Produce a report summarizing the analysis performed in this project. Ask the user their preferred format if unclear (Markdown file, Word doc via the `docx` skill, or an HTML artifact) — default to Markdown for a working draft.

## Report structure

```markdown
# Chapel Hill Yard Waste Cart & Pickup Fee — Analysis [Report/Summary]

## Question
What was actually being evaluated (e.g. is the yard waste cart/pickup fee reasonable given the Town's cost structure).

## Data sources
Documents used, with what each covers.

## Findings
The concrete numbers and what they show — cite page numbers. Separate clearly-established facts from inferences.

## Open questions / gaps
What's still unknown and why it matters (e.g. actual fee amount not yet located).

## Conclusion
A direct answer to the question, scoped honestly to what the data actually supports — don't overclaim if the fee schedule itself is still missing.
```

## Before finalizing

Run through the `verify` skill's checklist first — a writeup that repeats an unverified number or silently drops a known gap is worse than no writeup. If there are charts from `/six-charts`, reference or embed them rather than re-describing the data in prose.
