# app.py — Azerbaijan Cotton Yield Intelligence Dashboard
# Run: streamlit run app.py
import streamlit as st
import duckdb
import os

from dashboard_style import get_css, COLORS, COORDS, short
from dashboard_pages import page_overview, page_map, page_district, page_risk, page_model

# ── Config ────────────────────────────────────────────────────────────────────
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "cotton_project.duckdb")

st.set_page_config(
    page_title="Cotton Yield Intelligence · Azerbaijan",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Inject CSS ────────────────────────────────────────────────────────────────
st.markdown(get_css(), unsafe_allow_html=True)

# ── Load data ─────────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    con = duckdb.connect(DB_PATH, read_only=True)
    pred = con.execute("SELECT * FROM predictions").df()
    cotton = con.execute("SELECT * FROM clean_cotton").df()
    features = con.execute("SELECT * FROM features").df()
    con.close()

    bf_path = os.path.join(os.path.dirname(__file__), "models", "best_feature.txt")
    best_feat = "bolling_wind_mean"
    if os.path.exists(bf_path):
        with open(bf_path) as f:
            best_feat = f.read().strip()
    return pred, cotton, features, best_feat

predictions, cotton, features, best_feature = load_data()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        '<div class="sidebar-brand">'
        '<h1>🌾 Risk Masters</h1>'
        '<p>Cotton Yield Intelligence</p>'
        '</div>', unsafe_allow_html=True
    )
    st.markdown("---")

    page = st.radio(
        "Navigation",
        ["Overview", "Map View", "District Analysis", "Risk Heatmap", "Model Insights"],
        label_visibility="collapsed",
    )

    st.markdown("---")
    for label, val in [
        ("Districts", "15"), ("Years", "2000 – 2024"),
        ("Features", "42"), ("Growth Stages", "3"),
        ("Model", "Ridge CV"), ("Best Feature", best_feature),
    ]:
        st.markdown(
            f'<div class="sidebar-stat"><span>{label}</span><span class="val">{val}</span></div>',
            unsafe_allow_html=True,
        )

# ── Page Router ───────────────────────────────────────────────────────────────
if page == "Overview":
    page_overview(predictions, cotton, best_feature)
elif page == "Map View":
    page_map(predictions, COORDS)
elif page == "District Analysis":
    page_district(predictions, cotton)
elif page == "Risk Heatmap":
    page_risk(predictions)
elif page == "Model Insights":
    page_model(predictions, cotton, features, best_feature)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#475569; font-size:0.78rem; letter-spacing:0.5px;">'
    'Risk Masters · Azerbaijan Cotton Yield Intelligence · 2025 · '
    'Open-Meteo Archive API + 25-Year Cotton Production Dataset'
    '</p>', unsafe_allow_html=True
)