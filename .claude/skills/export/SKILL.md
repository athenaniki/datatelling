---
name: export
description: Export a table or extracted dataset from this project (e.g. Solid Waste division budget figures, any pandas DataFrame built during analysis) to CSV, Excel, or Parquet. Use when the user says "/export", asks to "save this as a spreadsheet/csv," or wants extracted budget data in a reusable file format.
---

# Export Data

Take whatever tabular data is currently in play (a pandas DataFrame built during this session, or a table just extracted from the budget PDF) and save it to disk in the format the user wants.

## Steps

1. If the user didn't specify a format, ask or default to `.xlsx` if the data has multiple related tables (one sheet per table), otherwise `.csv`.
2. Use pandas: `df.to_csv(path, index=False)`, `df.to_excel(path, index=False)`, or `df.to_parquet(path)`.
3. Keep dollar amounts as plain numeric values (not strings with `$`/commas) in the export — formatting is presentation, not data.
4. Name the file descriptively and place it in the project working directory (or wherever the user specifies), e.g. `solid-waste-budget-fy24-27.csv`.
5. Confirm what was exported: row/column count and the path.

If this is an .xlsx spreadsheet deliverable the user will hand to someone else (not just a working export), use the project's `xlsx` skill instead, which handles formatting, formulas, and polish.
