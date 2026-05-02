# dashboard_style.py — Theme & CSS for the premium dashboard
COLORS = {
    "bg": "#0A0E1A",
    "card": "#111827",
    "card_border": "#1E293B",
    "surface": "#0F172A",
    "text": "#E2E8F0",
    "text_muted": "#94A3B8",
    "green": "#10B981",
    "orange": "#F59E0B",
    "red": "#EF4444",
    "blue": "#3B82F6",
    "grid": "#1E293B",
    "bar_hist": "#334155",
}

PLOTLY_LAYOUT = dict(
    plot_bgcolor=COLORS["surface"], 
    paper_bgcolor=COLORS["surface"],
    font=dict(family="DM Sans, Inter, sans-serif", color=COLORS["text_muted"], size=12),
    yaxis=dict(gridcolor=COLORS["grid"], zerolinecolor=COLORS["grid"]),
    xaxis=dict(gridcolor=COLORS["grid"], zerolinecolor=COLORS["grid"]),
    margin=dict(l=50, r=30, t=60, b=50),
    hoverlabel=dict(bgcolor="#1E293B", font_size=13, font_color="#F1F5F9"),
)

def get_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&family=Syne:wght@600;700;800&display=swap');

/* ── Root ─────────────────────────────────────────── */
html, body, [data-testid="stAppViewContainer"], [data-testid="stApp"],
.main, .block-container, [data-testid="stMainBlockContainer"] {
    background-color: #0A0E1A !important;
    color: #E2E8F0 !important;
    font-family: 'DM Sans', sans-serif !important;
}
[data-testid="stHeader"] { background: transparent !important; }
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0F1629 0%, #0A0E1A 100%) !important;
    border-right: 1px solid #1E293B !important;
}
[data-testid="stSidebar"] * { color: #CBD5E1 !important; }

/* ── KPI Cards ────────────────────────────────────── */
div[data-testid="stMetric"] {
    background: linear-gradient(135deg, #111827 0%, #0F172A 100%);
    border: 1px solid #1E293B;
    border-radius: 12px;
    padding: 18px 20px;
    transition: all 0.3s ease;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
div[data-testid="stMetric"]:hover {
    border-color: #10B981;
    box-shadow: 0 0 25px rgba(16,185,129,0.15);
    transform: translateY(-2px);
}
div[data-testid="stMetric"] label { color: #94A3B8 !important; font-size: 0.8rem !important; letter-spacing: 0.5px; text-transform: uppercase; }
div[data-testid="stMetric"] [data-testid="stMetricValue"] { color: #F1F5F9 !important; font-family: 'DM Mono', monospace !important; font-size: 1.6rem !important; }

/* ── Insight boxes ────────────────────────────────── */
.insight-box {
    background: linear-gradient(135deg, rgba(16,185,129,0.08) 0%, rgba(16,185,129,0.03) 100%);
    border-left: 3px solid #10B981;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 12px 0 20px 0;
    font-size: 0.95rem;
    line-height: 1.6;
    color: #CBD5E1;
}
.warning-box {
    background: linear-gradient(135deg, rgba(239,68,68,0.08) 0%, rgba(239,68,68,0.03) 100%);
    border-left: 3px solid #EF4444;
    border-radius: 8px;
    padding: 16px 20px;
    margin: 12px 0 20px 0;
    color: #CBD5E1;
}

/* ── Section titles ───────────────────────────────── */
.section-title {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 2rem;
    background: linear-gradient(135deg, #F1F5F9 0%, #94A3B8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 8px;
}
.section-sub {
    color: #64748B;
    font-size: 0.9rem;
    margin-bottom: 24px;
    letter-spacing: 0.3px;
}

/* ── Sidebar brand ────────────────────────────────── */
.sidebar-brand {
    text-align: center;
    padding: 16px 0 8px 0;
}
.sidebar-brand h1 {
    font-family: 'Syne', sans-serif !important;
    font-size: 1.3rem !important;
    background: linear-gradient(135deg, #10B981 0%, #F59E0B 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 0 !important;
}
.sidebar-brand p {
    font-size: 0.72rem;
    color: #64748B !important;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin: 4px 0 0 0;
}
.sidebar-stat {
    background: #111827;
    border: 1px solid #1E293B;
    border-radius: 8px;
    padding: 10px 14px;
    margin: 4px 0;
    font-size: 0.82rem;
    display: flex;
    justify-content: space-between;
}
.sidebar-stat .val { color: #10B981; font-family: 'DM Mono', monospace; font-weight: 500; }

/* ── Misc ─────────────────────────────────────────── */
.stSelectbox > div > div { background-color: #111827 !important; border-color: #1E293B !important; }
.stRadio > div { gap: 2px !important; }
[data-testid="stDataFrame"] { border: 1px solid #1E293B; border-radius: 8px; overflow: hidden; }
div[data-testid="stTabs"] button { color: #94A3B8 !important; }
div[data-testid="stTabs"] button[aria-selected="true"] { color: #10B981 !important; border-bottom-color: #10B981 !important; }
hr { border-color: #1E293B !important; }
</style>
"""

COORDS = {
    "Goranboy district":  (40.61, 46.79),
    "Kurdamir district":  (40.34, 48.16),
    "Yevlakh district":   (40.62, 47.15),
    "Zardab district":    (40.22, 47.71),
    "Tartar district":    (40.34, 46.93),
    "Aghdam district":    (39.99, 46.93),
    "Sabirabad district": (40.01, 48.47),
    "Saatli district":    (39.93, 48.37),
    "Imishli district":   (39.87, 48.06),
    "Beylagan district":  (39.77, 47.62),
    "Aghjabadi district": (40.05, 47.46),
    "Barda district":     (40.37, 47.13),
    "Bilasuvar district": (39.46, 48.55),
    "Neftchala district": (39.38, 49.25),
    "Salyan district":    (39.60, 48.98),
}

def short(name):
    return name.replace(" district", "")
