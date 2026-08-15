"""Narration script, one entry per video segment. Text is adapted from site/index.html."""

SEGMENTS = [
    {
        "id": "01_title",
        "image": "01_title.png",
        "text": (
            "Did we overpay, or underpay, for our yard waste? "
            "This analysis covers Orange County, North Carolina, specifically the Town of "
            "Chapel Hill's yard waste collection program. Yard waste handling costs and "
            "collection rules have both been changing lately. Here's what the Town spends, "
            "what it charges, and how that compares, so you can decide for yourself."
        ),
    },
    {
        "id": "02_current_stats",
        "image": "02_current_stats.png",
        "text": (
            "Right now, a yard waste cart costs seventy five dollars. Loose brush or a large "
            "pile pickup costs one hundred twenty five dollars per truckload. The entire "
            "Solid Waste division's budget for the coming fiscal year is five point two nine "
            "million dollars, and staffing has stayed flat, at thirty four full time positions."
        ),
    },
    {
        "id": "chart_personnel_operating",
        "image": "chart_personnel_operating.png",
        "text": (
            "That budget covers all collection services together, trash, recycling, and yard "
            "waste, not yard waste alone. Most of it, about three point one million dollars, "
            "goes to personnel. The rest, roughly two point two million, covers operating "
            "costs like vehicles and supplies."
        ),
    },
    {
        "id": "chart_budget_trend",
        "image": "chart_budget_trend.png",
        "text": (
            "The division's total budget has been rising steadily year after year. The Town "
            "says this is driven by a retirement rate increase, a ten percent jump in "
            "insurance costs, standard salary increases, and more funding for vehicle "
            "replacement, not by expanding the service itself."
        ),
    },
    {
        "id": "chart_fee_history",
        "image": "chart_fee_history.png",
        "text": (
            "Despite those rising costs, something interesting happened to the fee itself. "
            "The Town had planned to raise the yard cart fee from seventy five dollars to one "
            "hundred dollars. Then it reversed that decision, and held the fee flat."
        ),
    },
    {
        "id": "chart_cost_vs_fee",
        "image": "chart_cost_vs_fee.png",
        "text": (
            "So the Solid Waste division's costs grew about four point seven percent, while "
            "the yard cart fee grew by exactly zero percent. Instead of raising the fee, the "
            "Town narrowed what it collects for free, ending free loose leaf vacuuming and "
            "charging for large brush piles."
        ),
    },
    {
        "id": "chart_peer_fees",
        "image": "chart_peer_fees.png",
        "text": (
            "But how does that seventy five dollar fee stack up nearby? In neighboring "
            "Carrboro, the same kind of yard waste cart costs fifty five dollars. Chapel "
            "Hill's fee runs about thirty six percent higher than its neighbor's."
        ),
    },
    {
        "id": "verdict_card",
        "image": "verdict_card.png",
        "text": (
            "So, here's the case both ways. In favor of reasonable: the fee stayed flat while "
            "costs rose, the cost drivers are routine, and staffing didn't grow. Against it: "
            "the fee is well above the neighboring town's, and free services quietly shrank "
            "instead of the fee going up."
        ),
    },
    {
        "id": "99_close",
        "image": "99_close.png",
        "text": (
            "So, overpaid, or underpaid? We don't have a public cost per cart figure to settle "
            "it completely, but the evidence is on the table. You decide."
        ),
    },
]
