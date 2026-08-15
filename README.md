# Chapel Hill Yard Waste Cart & Pickup Fee — Budget Rationale Analysis

## Project Goal
Evaluate whether the Town of Chapel Hill's yard waste cart fee and yard waste
pickup fee are reasonable, by tracing them back to the underlying cost
drivers in the Town's budget (staffing, equipment, operating costs) for the
Solid Waste Services division.

## Source Documents
- `fy2026-27-managers-recommended-budget.pdf` — Town of Chapel Hill,
  Manager's Recommended Budget, FY 2026-27 (132 pages). Covers General Fund
  departments, Debt, Transit, Stormwater, Parking, Capital Program, and
  other funds.

## Status: Fee data found (via townofchapelhill.org, not the budget PDF)

The Manager's Recommended Budget document does **not** contain a yard waste
cart fee or pickup fee schedule — confirmed by a full-text search of all 132
pages. The actual fee figures were sourced separately from
[chapelhillnc.gov's "Trash and Yard Waste" page](https://www.chapelhillnc.gov/Town-Services/Trash-and-Yard-Waste)
and [WRAL News (Oct 2025)](https://www.wral.com/news/local/chapel-hill-leaf-collection-policy-october-2025/):

| Fee | Amount | Note |
|---|---|---|
| Yard waste cart | $75 | Held flat for FY2026-27; a planned increase to $100 was reversed |
| Additional trash cart | $60 | First cart free |
| Loose brush / large pile pickup | $125/truckload | New as of July 1, 2026 — previously free weekly collection |

Effective July 1, 2026, the Town also stops accepting personal cans/mis-sorted
items (Town carts only, except paper bags allowed Nov–Jan leaf season).
Income-based financial assistance is available, including retroactive
refunds to July 1, 2025.

**Peer comparison**: Carrboro's equivalent yard waste cart fee is $55
(FY2025-26 fee schedule) — Chapel Hill's $75 is ~36% higher. Unincorporated
Orange County instead funds yard waste processing through a flat annual
Solid Waste Programs Fee per improved property, not a per-cart fee, so it
isn't directly comparable.

**Still open:** no yard-waste-specific cost-per-cart figure exists in the
Town's public budget (the Solid Waste division budget covers trash,
recycling, and yard waste together), and pre-2025 fee history wasn't
located, so we can't yet verify the $75 fee against an actual cost of
service or a longer fee trend.

## Website
A 3-tab site presenting this analysis ("Current Expense," "History v.
Current," "Reasonable v. Unreasonable") lives in [`site/`](site/index.html).
See [WEBSITE_PLAN.md](WEBSITE_PLAN.md) for the design plan.

## What the budget document does provide (Solid Waste Services division)

Source: Public Works Department section, pages 48-49 and 56.

| Metric | 2025-26 Budget | 2026-27 Recommended | % Change |
|---|---|---|---|
| Solid Waste division total | $5,110,290 | $5,287,768 | +4.7% |
| — Personnel | $2,947,264 | $3,104,540 | +5.3% |
| — Operating Costs | $2,102,910 | $2,183,228 | +3.8% |

**Staffing** (page 48): 34.0 FTE, unchanged year-over-year
- 1 Solid Waste Services Manager
- 1 Solid Waste Operations Coordinator
- 2 Solid Waste Crew Supervisors
- 17 Solid Waste Operators (Levels I-III)
- 13 Solid Waste Collectors

**Stated drivers of the increase** (page 56 narrative):
- Personnel (+5.3%): 0.75% retirement rate increase, 10% insurance cost
  increase, salary increase
- Operating (+3.8%): increased budget for vehicle replacement, added
  funding for supplies

**Related capital item** — Vehicle Replacement Fund (page 128): one rear
loader and one truck for Solid Waste are budgeted for replacement in
2026-27 as part of a $2,046,800 total fund.

## Analysis performed so far
The Solid Waste division's 4.7% expenditure increase is roughly in line
with (slightly below) the Public Works department's overall 5.2% increase,
and is attributable to routine, clearly identified cost drivers (benefits
and insurance inflation, a normal vehicle replacement cycle) rather than
service expansion or unexplained growth. Staffing levels are flat.

This supports the *cost side* being reasonable, but doesn't fully settle the
fee question, since the Solid Waste division budget covers all solid waste
services (trash, recycling, yard waste collectively), not yard waste alone,
and no per-cart cost allocation is broken out.

The fee itself was held flat (0% change) while division costs rose ~4.7% —
the Town appears to have absorbed cost growth into the fee rather than
raising it, instead narrowing free service scope (loose brush pickup now
costs $125/truckload, personal cans no longer accepted). Chapel Hill's $75
fee also runs ~36% above Carrboro's $55. See the site's "Reasonable v.
Unreasonable" tab for the full evidence breakdown both ways.

## Next Steps
1. Find pre-2025 yard cart fee history to see how $75 compares over a
   longer trend, not just this year's reversed increase.
2. Estimate cost-per-household or cost-per-cart from the Solid Waste
   division budget, if a yard-waste-specific cost breakdown or subscriber
   count can be found, to sanity-check the fee against actual cost recovery.
3. Expand peer comparison beyond Carrboro (e.g. Hillsborough, Durham) if
   more benchmarking is wanted.
