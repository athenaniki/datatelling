// Data mirrors /data/*.csv — kept inline so the page works over file:// without a server.
// Chart titles are omitted here — each chart sits inside an "Exhibit" block in the HTML
// that already carries a label + caption, so an in-chart title would just repeat it.

const BUDGET_TREND = [
  { period: "2024-25 Actual", total: 4860732, personnel: 2718518, operating: 2142214 },
  { period: "2025-26 Original", total: 5050174, personnel: 2947264, operating: 2102910 },
  { period: "2025-26 Revised", total: 5110290, personnel: 2947264, operating: 2163026 },
  { period: "2025-26 Estimated", total: 5113959, personnel: 2961341, operating: 2152618 },
  { period: "2026-27 Recommended", total: 5287768, personnel: 3104540, operating: 2183228 },
];

const FEE_HISTORY = [
  { period: "Through 2025-26", fee: 75, note: "Yard cart fee" },
  { period: "Planned (cancelled)", fee: 100, note: "Increase proposed for July 2026, then reversed" },
  { period: "2026-27 (actual)", fee: 75, note: "Held flat" },
];

const PEER_FEES = [
  { jurisdiction: "Carrboro", fee: 55 },
  { jurisdiction: "Chapel Hill", fee: 75 },
];

// Mirrors the CSS custom properties in css/style.css — Plotly can't read CSS vars directly.
const isDark = window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches;

const COLORS = isDark
  ? { green: "#6bad87", greenSoft: "#3c5b48", gold: "#d3a656", navy: "#8fadcc", ink: "#e9ede2" }
  : { green: "#1f5c3e", greenSoft: "#7ba98c", gold: "#9c7220", navy: "#24405f", ink: "#1a231e" };

const paperColor = isDark ? "#191f16" : "#ffffff";
const gridColor = isDark ? "#333f2b" : "#e3e8d8";
const FONT = "'Public Sans', -apple-system, Helvetica, Arial, sans-serif";
const FONT_MONO = "'IBM Plex Mono', ui-monospace, monospace";

const baseLayout = {
  paper_bgcolor: paperColor,
  plot_bgcolor: paperColor,
  font: { color: COLORS.ink, family: FONT, size: 13 },
  margin: { t: 38, r: 24, l: 60, b: 46 },
  xaxis: { gridcolor: gridColor, zeroline: false },
  yaxis: { gridcolor: gridColor, zeroline: false },
  bargap: 0.4,
};

const rendered = { current: false, history: false, verdict: false };

function money(n) {
  return "$" + Math.round(n).toLocaleString();
}

const numberFont = { family: FONT_MONO, size: 15 };

function renderCurrentExpenseCharts() {
  if (rendered.current) return;
  rendered.current = true;

  const latest = BUDGET_TREND[BUDGET_TREND.length - 1];
  Plotly.newPlot(
    "chart-personnel-operating",
    [
      {
        type: "bar",
        x: ["Personnel", "Operating"],
        y: [latest.personnel, latest.operating],
        marker: { color: [COLORS.green, COLORS.greenSoft] },
        text: [money(latest.personnel), money(latest.operating)],
        textposition: "outside",
        textfont: numberFont,
      },
    ],
    {
      ...baseLayout,
      yaxis: { ...baseLayout.yaxis, title: "Dollars", tickprefix: "$" },
    },
    { displayModeBar: false, responsive: true }
  );
}

function renderHistoryCharts() {
  if (rendered.history) return;
  rendered.history = true;

  Plotly.newPlot(
    "chart-budget-trend",
    [
      {
        type: "scatter",
        mode: "lines+markers",
        name: "Total Solid Waste division spend",
        x: BUDGET_TREND.map((d) => d.period),
        y: BUDGET_TREND.map((d) => d.total),
        line: { color: COLORS.green, width: 3 },
        marker: { size: 8, color: COLORS.green },
      },
    ],
    {
      ...baseLayout,
      yaxis: { ...baseLayout.yaxis, title: "Dollars", tickprefix: "$", rangemode: "tozero" },
    },
    { displayModeBar: false, responsive: true }
  );

  Plotly.newPlot(
    "chart-fee-history",
    [
      {
        type: "bar",
        x: FEE_HISTORY.map((d) => d.period),
        y: FEE_HISTORY.map((d) => d.fee),
        marker: {
          color: FEE_HISTORY.map((d) => (d.note.includes("cancelled") ? COLORS.gold : COLORS.green)),
        },
        text: FEE_HISTORY.map((d) => "$" + d.fee),
        textposition: "outside",
        textfont: numberFont,
        hovertext: FEE_HISTORY.map((d) => d.note),
      },
    ],
    {
      ...baseLayout,
      yaxis: { ...baseLayout.yaxis, title: "Dollars per cart", tickprefix: "$", range: [0, 120] },
    },
    { displayModeBar: false, responsive: true }
  );
}

function renderVerdictCharts() {
  if (rendered.verdict) return;
  rendered.verdict = true;

  const costChangePct =
    ((BUDGET_TREND[BUDGET_TREND.length - 1].total - BUDGET_TREND[1].total) / BUDGET_TREND[1].total) * 100;

  Plotly.newPlot(
    "chart-cost-vs-fee",
    [
      {
        type: "bar",
        x: ["Division cost change<br>(FY25-26 → FY26-27)", "Yard cart fee change<br>(same period)"],
        y: [Number(costChangePct.toFixed(1)), 0],
        marker: { color: [COLORS.gold, COLORS.green] },
        text: [`+${costChangePct.toFixed(1)}%`, "0% (held flat)"],
        textposition: "outside",
        textfont: numberFont,
      },
    ],
    {
      ...baseLayout,
      yaxis: { ...baseLayout.yaxis, title: "% change", ticksuffix: "%", range: [-5, Math.max(costChangePct + 3, 10)] },
    },
    { displayModeBar: false, responsive: true }
  );

  Plotly.newPlot(
    "chart-peer-fees",
    [
      {
        type: "bar",
        x: PEER_FEES.map((d) => d.jurisdiction),
        y: PEER_FEES.map((d) => d.fee),
        marker: { color: PEER_FEES.map((d) => (d.jurisdiction === "Chapel Hill" ? COLORS.gold : COLORS.green)) },
        text: PEER_FEES.map((d) => "$" + d.fee),
        textposition: "outside",
        textfont: numberFont,
      },
    ],
    {
      ...baseLayout,
      yaxis: { ...baseLayout.yaxis, title: "Dollars per cart", tickprefix: "$", range: [0, 90] },
    },
    { displayModeBar: false, responsive: true }
  );
}

window.renderChartsFor = function (tabId) {
  if (tabId === "tab-current") renderCurrentExpenseCharts();
  if (tabId === "tab-history") renderHistoryCharts();
  if (tabId === "tab-verdict") renderVerdictCharts();
};

document.addEventListener("DOMContentLoaded", () => {
  // Render the first visible tab immediately.
  renderCurrentExpenseCharts();
});
