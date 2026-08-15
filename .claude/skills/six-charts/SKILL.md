---
name: six-charts
description: Generate six varied Plotly charts from tabular data in this project (e.g. Solid Waste division budget figures, extracted PDF tables, or any CSV/Excel the user points to). Use whenever the user says "/six-charts", asks for a quick set of charts, wants to "see the data visually," or wants several different views of a budget/fee dataset fast. Produces one self-contained HTML file with six distinct chart types, not six copies of the same chart.
---

# Six Charts

Produce six different, complementary Plotly visualizations of a dataset in one pass, so the user gets broad visual coverage without asking for each chart individually.

## When invoked

1. Identify the dataset. If the user didn't name one, use the most recently extracted/exported table in this project (check for CSVs in the working directory, or re-extract from `fy2026-27-managers-recommended-budget.pdf` using pypdf/pdfplumber if nothing else exists).
2. Look at the columns and pick **six genuinely different angles**, not six bar charts. Draw from this pool and pick what fits the data — don't force a chart type that doesn't suit the columns available:
   - Trend over time (line chart) — e.g. Solid Waste division spend across 2024-25 Actual → 2026-27 Recommended
   - Category comparison (bar chart) — e.g. expenditures by division within Public Works
   - Composition (stacked bar or treemap) — e.g. Personnel vs Operating Costs breakdown
   - Change/variance (waterfall or diverging bar) — e.g. % change year over year by line item
   - Distribution (histogram or box plot) — only if there are enough data points to make this meaningful
   - Relationship (scatter) — e.g. FTE count vs division budget, if both are available
3. Build each chart with `plotly.express` or `plotly.graph_objects` in Python. Use `fig.write_html(..., include_plotlyjs="cdn")` per chart, or better: combine all six into one HTML page using subplots (`plotly.subplots.make_subplots`) or by concatenating each `fig.to_html(full_html=False, include_plotlyjs="cdn")` into a single page with a shared `<head>`.
4. Title each chart plainly (what it shows, not just the column name) and label axes with units (e.g. "$", "%", "FTE").
5. Save the output as a single `.html` file in the project directory, named descriptively (e.g. `solid-waste-six-charts.html`), and open/send it to the user.

## Notes specific to this project
- Budget figures in the source PDF are often formatted with `$` and commas as strings — strip and cast to float before plotting.
- When comparing years, use the "Recommended" column as the forward-looking value and "Actual"/"Original Budget" for history — don't mix "Estimated" (a mid-year projection) into a multi-year trend line without labeling it distinctly.
- If the dataset is small (e.g. just 5 division rows), it's fine for two of the six charts to be simple table-like visuals (e.g. an annotated bar with value labels) rather than forcing complex chart types onto too little data.
