---
name: dash-app
description: Build an interactive Plotly Dash web app summarizing this project's budget/yard-waste-fee analysis, for exploring the data (filters, drill-downs) rather than a static report. Use when the user says "/dash-app", asks for a "dashboard," "interactive app," or wants to explore the budget data themselves rather than just see a fixed chart or report.
---

# Dash App

Build a small, self-contained Plotly Dash app for interactively exploring this project's budget data (e.g. Solid Waste / Public Works division trends, any extracted fee data).

## Steps

1. Confirm scope with the user if it's ambiguous: what should be explorable (division, year range, chart type)?
2. Structure as a single `app.py`:
   - Load data (from an exported CSV — use the `export` skill first if nothing's been exported yet).
   - Layout: a title, 1-2 filter controls (e.g. `dcc.Dropdown` for division, `dcc.RangeSlider` for years), and a `dcc.Graph` that updates via callback.
   - Keep it to one page — this is a working exploration tool, not a polished product.
3. Run it locally (`python app.py`, default Dash port 8050) and use the browser preview tool to open and verify it actually renders and the filters work before telling the user it's done.
4. Tell the user how to run it themselves (`python app.py` from the project directory) and what port to open.

## Notes
- Don't over-engineer: no auth, no deployment config, no multi-page routing unless asked. This is for the user's own local exploration of the budget data.
- If the user wants something to *share* with others (not just explore themselves), a static HTML export (see `six-charts`) or a proper report (see `writeup`) is usually the better fit — check which they actually want before building a full Dash app.
