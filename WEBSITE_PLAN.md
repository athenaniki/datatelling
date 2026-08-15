# Website Plan: "Did we overpay or underpay for our yard waste?"

## Purpose
A small data-presentation website (not an app with accounts/backend) that
lets an Orange County, NC resident look at the numbers behind Chapel Hill's
yard waste handling cost and form their own judgment on whether it's
reasonable. Data-forward, verdict-neutral — present evidence, invite the
user to conclude "overcharged," "fair," or "underpaying and should be
grateful," rather than declaring an answer for them.

## Page structure

### Header (all tabs)
- **Title**: "Did we overpay or underpay for our yard waste?"
- **Intro paragraph** (directly under title), e.g.:
  > This analysis covers Orange County, North Carolina — specifically the
  > Town of Chapel Hill's yard waste collection program. Yard waste
  > handling costs have risen in recent years. This page walks through
  > what the Town spends, how that compares to history, and lets you
  > weigh in on whether the current fee is reasonable.
  - Should state clearly: this is independent analysis of public budget
    documents, not an official Town publication.
  - Should name the source document(s) and the fiscal year covered.

### Tab 1 — Current Expense
What does yard waste collection cost right now, and what does the
resident pay?
- Current yard waste cart fee / pickup fee (dollar amount) — **BLOCKED**,
  see Open Data Gaps below.
- Current-year Solid Waste division budget: total, Personnel vs.
  Operating split ([README.md](README.md) already has FY2026-27 figures).
- If a per-household or per-cart cost can be derived (division budget ÷
  number of carts/subscribers, if that count is published), show it next
  to the actual fee as a sanity check.
- Visual: a simple stat-tile row (division total, per-FTE cost, fee
  amount if found) plus one bar chart breaking down Personnel vs.
  Operating costs.

### Tab 2 — History vs. Current
Is this year's cost/fee an outlier or a continuation of a trend?
- Multi-year trend line of Solid Waste division expenditures (the budget
  PDF gives 2024-25 Actual, 2025-26 Original/Revised/Estimated, 2026-27
  Recommended — enough for a short trend, longer history would need prior
  years' budget books if available).
- If historical fee amounts can be found (past fee schedules/ordinances),
  a second line or table showing fee-over-time alongside cost-over-time —
  this is the chart that actually answers "did the fee track the cost."
- Call out stated cost drivers from the budget narrative (retirement rate
  increase, insurance increase, salary increase, vehicle replacement) so
  the trend isn't just numbers with no explanation.

### Tab 3 — Reasonable vs. Unreasonable
The "you decide" tab — lay out the comparison points a reader would use
to judge, without asserting a verdict.
- Cost growth rate (Solid Waste division %) vs. general inflation / CPI
  for the same period, and vs. the fee change % (once known).
- Whether staffing grew, shrank, or stayed flat while cost rose (flat
  staffing + rising cost = benefits/insurance/equipment driven, which
  reads differently than cost rising because service expanded).
- Optional: peer comparison — yard waste fees in similar NC
  municipalities/Orange County towns, if the user wants to gather that.
- Framing device: two labeled columns or a simple slider/toggle —
  "Evidence it's reasonable" / "Evidence it's not" — populated from the
  actual findings, letting the reader weigh them rather than the site
  declaring a winner.
- Explicit "what we don't know" note if the fee amount itself is still
  unconfirmed — the reader should see the analysis is partial, not be
  left to assume it's complete.

## Data pipeline
1. Extract relevant tables from `fy2026-27-managers-recommended-budget.pdf`
   (already done for Solid Waste division — see [README.md](README.md)).
2. Locate and extract the actual yard waste cart/pickup fee schedule
   (still missing — see Open Data Gaps).
3. Export cleaned tables to CSV (`/export` skill) for the site to consume.
4. Run `/data-quality` and `/spot-check` skills on extracted numbers
   before they go on the page.
5. Build charts with Plotly (project already has `/six-charts` and
   `/dash-app` skills set up for this).

## Tech approach (proposed, needs confirmation)
- **Static site**: plain HTML/CSS/JS with Plotly.js charts, no backend
  needed since this is public budget data, not user data. Simplest to
  build and to host.
- **Hosting**: GitHub Pages off the existing `datatelling` repo
  (already linked as `origin` — [github.com/athenaniki/datatelling](https://github.com/athenaniki/datatelling.git)),
  since no server/database is required.
- **Structure**:
  ```
  /site
    index.html          (tab shell + header/intro)
    /data
      solid-waste-budget.csv
      yard-waste-fee-history.csv   (once located)
    /js
      charts.js
      tabs.js
    /css
      style.css
  ```
- Tabs implemented as simple client-side show/hide (no routing needed for
  3 tabs) — no framework required unless the user wants one.

## Open Data Gaps (must resolve before Tab 1/3 are complete)
- **Actual yard waste cart fee and pickup fee amounts** — not present in
  the Manager's Recommended Budget PDF (confirmed by full-text search).
  Needed from the Town's separate Fee Schedule / rate resolution.
- **Historical fee amounts** (prior years) — needed for Tab 2's
  fee-over-time comparison to be meaningful, not just cost-over-time.
- **Number of yard waste cart subscribers/households served** — needed to
  compute a per-household or per-cart cost for the Tab 1 sanity check.
- **Peer municipality fees** (optional) — only needed if Tab 3 includes a
  peer-comparison column.

## Open questions for the user
1. Confirm the tech approach above (static HTML/Plotly/GitHub Pages) or
   prefer something else (e.g. a React app, a no-code tool)?
2. Do you already have or know where to get the Town's Fee Schedule
   document, or should that be researched next?
3. Want the "Reasonable vs. Unreasonable" tab to include a peer-city
   comparison, or keep it scoped to Chapel Hill's own numbers?
4. Any visual/brand preferences (colors, tone — serious/civic vs.
   more playful data-story style)?

## Suggested build order
1. Resolve the fee-schedule data gap (blocks Tab 1 and most of Tab 3).
2. Build the static site shell (header, intro, 3-tab nav) with
   placeholder content.
3. Wire in Tab 1 (current expense) once fee data is in.
4. Wire in Tab 2 (history vs. current) from existing multi-year budget
   data.
5. Wire in Tab 3 (reasonable vs. unreasonable) last, since it synthesizes
   Tabs 1 and 2.
6. Run `/verify` skill before publishing.
