"""Generate 1920x1080 chart and title-card PNGs for the yard waste video."""
import plotly.graph_objects as go
from PIL import Image, ImageDraw, ImageFont
import os

OUT = os.path.join(os.path.dirname(__file__), "frames")
os.makedirs(OUT, exist_ok=True)

W, H = 1920, 1080

BG = "#faf8f5"
TEXT = "#2b2620"
MUTED = "#6b6255"
ACCENT = "#2f6b4f"
ACCENT_SOFT = "#8fc6ab"
WARN = "#b5502f"

FONT_DIR = "/System/Library/Fonts/Supplemental"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


def title_card(filename, title, subtitle=None, footer=None):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    title_font = font("Arial Bold.ttf", 84)
    sub_font = font("Arial.ttf", 40)
    foot_font = font("Arial.ttf", 30)

    # wrap title
    words = title.split()
    lines, cur = [], ""
    for w_ in words:
        test = (cur + " " + w_).strip()
        if d.textlength(test, font=title_font) > W - 240:
            lines.append(cur)
            cur = w_
        else:
            cur = test
    lines.append(cur)

    total_h = len(lines) * 100
    y = (H - total_h) / 2 - (60 if subtitle else 0)
    for line in lines:
        w_ = d.textlength(line, font=title_font)
        d.text(((W - w_) / 2, y), line, font=title_font, fill=TEXT)
        y += 100

    if subtitle:
        y += 40
        words = subtitle.split()
        lines, cur = [], ""
        for w_ in words:
            test = (cur + " " + w_).strip()
            if d.textlength(test, font=sub_font) > W - 400:
                lines.append(cur)
                cur = w_
            else:
                cur = test
        lines.append(cur)
        for line in lines:
            w_ = d.textlength(line, font=sub_font)
            d.text(((W - w_) / 2, y), line, font=sub_font, fill=MUTED)
            y += 58

    if footer:
        w_ = d.textlength(footer, font=foot_font)
        d.text(((W - w_) / 2, H - 90), footer, font=foot_font, fill=MUTED)

    img.save(os.path.join(OUT, filename))


def stat_card(filename, heading, stats):
    """stats: list of (value, label, color)"""
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    head_font = font("Arial Bold.ttf", 64)
    val_font = font("Arial Bold.ttf", 90)
    label_font = font("Arial.ttf", 34)

    w_ = d.textlength(heading, font=head_font)
    d.text(((W - w_) / 2, 100), heading, font=head_font, fill=TEXT)

    n = len(stats)
    tile_w, tile_h = 420, 320
    gap = 60
    total_w = n * tile_w + (n - 1) * gap
    x0 = (W - total_w) / 2
    y0 = 420

    for i, (value, label, color) in enumerate(stats):
        x = x0 + i * (tile_w + gap)
        d.rounded_rectangle([x, y0, x + tile_w, y0 + tile_h], radius=24, fill="#ffffff", outline="#e3ddd3", width=2)
        vw = d.textlength(value, font=val_font)
        d.text((x + (tile_w - vw) / 2, y0 + 70), value, font=val_font, fill=color)
        # wrap label
        words = label.split()
        lines, cur = [], ""
        for w2 in words:
            test = (cur + " " + w2).strip()
            if d.textlength(test, font=label_font) > tile_w - 40:
                lines.append(cur)
                cur = w2
            else:
                cur = test
        lines.append(cur)
        ly = y0 + 190
        for line in lines:
            lw = d.textlength(line, font=label_font)
            d.text((x + (tile_w - lw) / 2, ly), line, font=label_font, fill=MUTED)
            ly += 42

    img.save(os.path.join(OUT, filename))


def plotly_layout(title):
    return dict(
        title=dict(text=title, font=dict(size=34, color=TEXT), x=0.5),
        paper_bgcolor=BG,
        plot_bgcolor="#ffffff",
        font=dict(color=TEXT, family="Arial", size=22),
        margin=dict(t=90, r=60, l=100, b=80),
        width=W,
        height=H,
    )


def chart_personnel_operating():
    fig = go.Figure(
        go.Bar(
            x=["Personnel", "Operating"],
            y=[3104540, 2183228],
            marker_color=[ACCENT, ACCENT_SOFT],
            text=["$3,104,540", "$2,183,228"],
            textposition="outside",
            textfont=dict(size=26),
        )
    )
    fig.update_layout(**plotly_layout("FY2026-27 Solid Waste Division: Personnel vs. Operating"))
    fig.update_yaxes(title="Dollars", tickprefix="$", gridcolor="#e3ddd3")
    fig.write_image(os.path.join(OUT, "chart_personnel_operating.png"))


def chart_budget_trend():
    periods = ["2024-25\nActual", "2025-26\nOriginal", "2025-26\nRevised", "2025-26\nEstimated", "2026-27\nRecommended"]
    totals = [4860732, 5050174, 5110290, 5113959, 5287768]
    fig = go.Figure(
        go.Scatter(
            x=periods, y=totals, mode="lines+markers+text",
            line=dict(color=ACCENT, width=5),
            marker=dict(size=14),
            text=[f"${v:,.0f}" for v in totals],
            textposition="top center",
            textfont=dict(size=20),
        )
    )
    fig.update_layout(**plotly_layout("Solid Waste Division Total Expenditure Over Time"))
    fig.update_yaxes(title="Dollars", tickprefix="$", rangemode="tozero", gridcolor="#e3ddd3")
    fig.write_image(os.path.join(OUT, "chart_budget_trend.png"))


def chart_fee_history():
    periods = ["Through\n2025-26", "Planned\n(cancelled)", "2026-27\n(actual)"]
    fees = [75, 100, 75]
    colors = [ACCENT, WARN, ACCENT]
    fig = go.Figure(
        go.Bar(
            x=periods, y=fees, marker_color=colors,
            text=[f"${v}" for v in fees], textposition="outside", textfont=dict(size=28),
        )
    )
    fig.update_layout(**plotly_layout("Yard Waste Cart Fee: Planned vs. Actual"))
    fig.update_yaxes(title="Dollars per cart", tickprefix="$", range=[0, 120], gridcolor="#e3ddd3")
    fig.write_image(os.path.join(OUT, "chart_fee_history.png"))


def chart_cost_vs_fee():
    fig = go.Figure(
        go.Bar(
            x=["Division cost change<br>(FY25-26 → FY26-27)", "Yard cart fee change<br>(same period)"],
            y=[4.7, 0],
            marker_color=[WARN, ACCENT],
            text=["+4.7%", "0% (held flat)"], textposition="outside", textfont=dict(size=28),
        )
    )
    fig.update_layout(**plotly_layout("Cost Growth vs. Fee Growth"))
    fig.update_yaxes(title="% change", ticksuffix="%", range=[-2, 8], gridcolor="#e3ddd3")
    fig.write_image(os.path.join(OUT, "chart_cost_vs_fee.png"))


def chart_peer_fees():
    fig = go.Figure(
        go.Bar(
            x=["Carrboro", "Chapel Hill"], y=[55, 75],
            marker_color=[ACCENT, WARN],
            text=["$55", "$75"], textposition="outside", textfont=dict(size=28),
        )
    )
    fig.update_layout(**plotly_layout("Yard Waste Cart Fee: Chapel Hill vs. Carrboro"))
    fig.update_yaxes(title="Dollars per cart", tickprefix="$", range=[0, 90], gridcolor="#e3ddd3")
    fig.write_image(os.path.join(OUT, "chart_peer_fees.png"))


def verdict_card():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    head_font = font("Arial Bold.ttf", 60)
    col_head_font = font("Arial Bold.ttf", 40)
    body_font = font("Arial.ttf", 30)

    heading = "You decide."
    hw = d.textlength(heading, font=head_font)
    d.text(((W - hw) / 2, 80), heading, font=head_font, fill=TEXT)

    col_w = 780
    gap = 100
    x0 = (W - (col_w * 2 + gap)) / 2
    y0 = 230
    col_h = 720

    d.rounded_rectangle([x0, y0, x0 + col_w, y0 + col_h], radius=24, fill="#ffffff", outline="#e3ddd3", width=2)
    d.text((x0 + 40, y0 + 40), "Reasonable", font=col_head_font, fill=ACCENT)
    reasonable = [
        "Fee held flat at $75 while",
        "division costs rose ~4.7%",
        "",
        "Routine cost drivers:",
        "retirement, insurance, salaries",
        "",
        "Staffing flat at 34.0 FTE",
        "",
        "Financial assistance available",
    ]
    ly = y0 + 130
    for line in reasonable:
        d.text((x0 + 40, ly), line, font=body_font, fill=TEXT)
        ly += 48

    x1 = x0 + col_w + gap
    d.rounded_rectangle([x1, y0, x1 + col_w, y0 + col_h], radius=24, fill="#ffffff", outline="#e3ddd3", width=2)
    d.text((x1 + 40, y0 + 40), "Not so reasonable", font=col_head_font, fill=WARN)
    unreasonable = [
        "$75 is ~36% above",
        "Carrboro's $55 fee",
        "",
        "Free service scope shrank:",
        "brush piles now $125/load",
        "",
        "No public per-cart cost data",
        "to verify against",
    ]
    ly = y0 + 130
    for line in unreasonable:
        d.text((x1 + 40, ly), line, font=body_font, fill=TEXT)
        ly += 48

    img.save(os.path.join(OUT, "verdict_card.png"))


if __name__ == "__main__":
    title_card(
        "01_title.png",
        "Did we overpay or underpay for our yard waste?",
        "An independent look at Chapel Hill, Orange County, North Carolina",
    )
    stat_card(
        "02_current_stats.png",
        "What it costs right now",
        [
            ("$75", "Yard waste cart fee", ACCENT),
            ("$125", "Brush pickup per truckload", WARN),
            ("$5.29M", "FY26-27 division budget", TEXT),
            ("34.0", "Division FTE staff, flat", TEXT),
        ],
    )
    chart_personnel_operating()
    chart_budget_trend()
    chart_fee_history()
    chart_cost_vs_fee()
    chart_peer_fees()
    verdict_card()
    title_card(
        "99_close.png",
        "So — overpaid, or underpaid?",
        "The evidence is on the table. You decide.",
        footer="Sources: Town of Chapel Hill FY2026-27 Budget, chapelhillnc.gov, WRAL News, Town of Carrboro Fee Schedule",
    )
    print("Slides generated in", OUT)
