# dashboard_pages.py — All five page renderers
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from dashboard_style import COLORS, PLOTLY_LAYOUT, short

# ═══════════════════════════════════════════════════════════════════════════════
#  HELPER
# ═══════════════════════════════════════════════════════════════════════════════
def _layout(**kw):
    """Merge base PLOTLY_LAYOUT with overrides."""
    base = {k: v.copy() if isinstance(v, dict) else v for k, v in PLOTLY_LAYOUT.items()}
    for k, v in kw.items():
        if isinstance(v, dict) and k in base and isinstance(base[k], dict):
            base[k].update(v)
        else:
            base[k] = v
    return base 


# ═══════════════════════════════════════════════════════════════════════════════
#  1 · OVERVIEW
# ═══════════════════════════════════════════════════════════════════════════════
def page_overview(predictions, cotton, best_feature):
    st.markdown('<p class="section-title">Azerbaijan Cotton Yield Forecast </p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Predicted yield, historical comparison, and risk overview across 15 districts</p>', unsafe_allow_html=True)

    pred_valid = predictions.dropna(subset=["pred_yield"])
    total_pred = pred_valid["pred_yield"].sum()
    total_hist = pred_valid["avg_yield"].sum()
    pct_chg = ((total_pred - total_hist) / total_hist) * 100
    risk_cols = ["squaring_risk_pct", "flowering_risk_pct", "bolling_risk_pct"]
    avg_risk = predictions[risk_cols].mean().mean()
    best_d = pred_valid.loc[pred_valid["pred_yield"].idxmax(), "region"]

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Total Predicted 2025", f"{total_pred:,.0f} t")
    c2.metric("Historical Average", f"{total_hist:,.0f} t")
    c3.metric("Overall Change", f"{pct_chg:+.1f} %")
    c4.metric("Top District", short(best_d))

    st.markdown(
        '<div class="insight-box">'
        '🔬 <strong>Key Finding:</strong> Cotton yield is driven mostly by <strong>district baseline</strong> (~70 % of variance). '
        'During <strong>flowering (DOY 196–243, Jul–Aug)</strong>, night temperature becomes the '
        'dominant weather signal — high nights cause boll shedding and yield loss. '
        f'Best single predictor: <code>{best_feature}</code>.'
        '</div>', unsafe_allow_html=True
    )

    # ── Bar chart ─────────────────────────────────────────────────────────────
    ps = pred_valid.sort_values("pred_yield", ascending=False)
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Historical Avg", x=[short(r) for r in ps["region"]], y=ps["avg_yield"],
        marker_color=COLORS["bar_hist"], marker_line_width=0,
        hovertemplate="%{x}<br>Historical: %{y:.1f} t<extra></extra>",
    ))
    fig.add_trace(go.Bar(
        name="2025 Prediction", x=[short(r) for r in ps["region"]], y=ps["pred_yield"],
        marker_color=[COLORS["green"] if p >= h else COLORS["red"] for p, h in zip(ps["pred_yield"], ps["avg_yield"])],
        marker_line_width=0,
        hovertemplate="%{x}<br>Predicted: %{y:.1f} t<extra></extra>",
    ))
    fig.update_layout(**_layout(
        barmode="group", title="2025 Predicted vs Historical Average Yield",
        legend=dict(orientation="h", y=1.12, x=0.5, xanchor="center"),
        yaxis=dict(title="Yield (tonnes)", gridcolor=COLORS["grid"]),
        height=420,
    ))
    st.plotly_chart(fig, width="stretch")

    # ── Data table ────────────────────────────────────────────────────────────
    tbl = predictions[["region", "pred_yield", "avg_yield", "pct_change"] + risk_cols].copy()
    tbl.columns = ["District", "Pred (t)", "Avg (t)", "Chg %", "Squar %", "Flow %", "Boll %"]
    tbl["District"] = tbl["District"].apply(short)
    st.dataframe(
        tbl.reset_index(drop=True).style
        .format({"Pred (t)": "{:.1f}", "Avg (t)": "{:.1f}", "Chg %": "{:+.1f}",
                 "Squar %": "{:.0f}", "Flow %": "{:.0f}", "Boll %": "{:.0f}"}, na_rep="—")
        .background_gradient(subset=["Chg %"], cmap="RdYlGn", vmin=-30, vmax=30)
        .background_gradient(subset=["Squar %", "Flow %", "Boll %"], cmap="RdYlGn_r", vmin=0, vmax=100),
        width="stretch", height=420,
    )


# ═══════════════════════════════════════════════════════════════════════════════
#  2 · MAP VIEW
# ═══════════════════════════════════════════════════════════════════════════════
def page_map(predictions, coords):
    st.markdown('<p class="section-title">Geographic Yield Distribution — 2025</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Interactive map · bubble size = yield magnitude · colour gradient = performance</p>', unsafe_allow_html=True)

    df = predictions.copy()
    df["lat"] = df["region"].map(lambda x: coords.get(x, (0, 0))[0])
    df["lon"] = df["region"].map(lambda x: coords.get(x, (0, 0))[1])
    df["label"] = df["region"].apply(short)
    df["pred_yield_display"] = df["pred_yield"].fillna(0)
    df["flowering_risk_display"] = df["flowering_risk_pct"].fillna(0)

    tab1, tab2 = st.tabs(["🌾 Predicted Yield", "⚠️ Flowering Risk"])

    with tab1:
        fig = px.scatter_mapbox(
            df, lat="lat", lon="lon", size="pred_yield_display", color="pred_yield_display",
            hover_name="label",
            hover_data={"pred_yield_display": (":.1f"), "avg_yield": ":.1f", "pct_change": ":.1f", "lat": False, "lon": False},
            color_continuous_scale=["#EF4444", "#F59E0B", "#10B981"],
            size_max=38, zoom=6.2, center={"lat": 40.0, "lon": 47.9},
            labels={"pred_yield_display": "Predicted Yield (t)"},
        )
        fig.update_layout(
            mapbox_style="carto-darkmatter",
            paper_bgcolor=COLORS["surface"], font=dict(color=COLORS["text_muted"]),
            height=600, margin=dict(l=0, r=0, t=10, b=0),
            coloraxis_colorbar=dict(title="Yield (t)", thickness=15, len=0.6),
        )
        st.plotly_chart(fig, width="stretch")

    with tab2:
        fig2 = px.scatter_mapbox(
            df, lat="lat", lon="lon", size="flowering_risk_display", color="flowering_risk_display",
            hover_name="label",
            hover_data={"flowering_risk_display": ":.0f", "lat": False, "lon": False},
            color_continuous_scale=["#10B981", "#F59E0B", "#EF4444"],
            size_max=38, zoom=6.2, center={"lat": 40.0, "lon": 47.9},
            labels={"flowering_risk_display": "Flowering Risk %"},
        )
        fig2.update_layout(
            mapbox_style="carto-darkmatter",
            paper_bgcolor=COLORS["surface"], font=dict(color=COLORS["text_muted"]),
            height=600, margin=dict(l=0, r=0, t=10, b=0),
            coloraxis_colorbar=dict(title="Risk %", thickness=15, len=0.6),
        )
        st.plotly_chart(fig2, width="stretch")


# ═══════════════════════════════════════════════════════════════════════════════
#  3 · DISTRICT ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════
def page_district(predictions, cotton):
    st.markdown('<p class="section-title">District Deep Dive</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Historical trend, 2025 forecast, and stage-level risk for each district</p>', unsafe_allow_html=True)

    district = st.selectbox("Select District", sorted(predictions["region"].unique()), format_func=short)
    dp = predictions[predictions["region"] == district].iloc[0]
    dh = cotton[cotton["region"] == district].sort_values("year")

    c1, c2, c3 = st.columns(3)
    pred_val = dp["pred_yield"]
    pred_str = f"{pred_val:.1f} t" if pd.notna(pred_val) else "N/A (excluded)"
    chg_str = f"{dp['pct_change']:+.1f} % vs avg" if pd.notna(dp["pct_change"]) else "excluded from model"
    c1.metric("2025 Prediction", pred_str, chg_str)
    c2.metric("Historical Average", f"{dp['avg_yield']:.1f} t", f"σ = {dh['yield_tonnes'].std():.1f} t")
    avg_risk = np.mean([dp["squaring_risk_pct"], dp["flowering_risk_pct"], dp["bolling_risk_pct"]])
    c3.metric("Avg Stage Risk", f"{avg_risk:.0f} %")

    # ── Time series ───────────────────────────────────────────────────────────
    fig = go.Figure()
    fig.add_vrect(x0=2018.5, x1=2021.5, fillcolor=COLORS["red"], opacity=0.07, line_width=0,
                  annotation_text="Structural Break", annotation_position="top left",
                  annotation_font=dict(size=11, color=COLORS["red"], family="DM Mono"))
    fig.add_hline(y=dp["avg_yield"], line_dash="dot", line_color="#475569", line_width=1,
                  annotation_text=f"avg {dp['avg_yield']:.1f} t",
                  annotation_font=dict(color="#64748B", size=10))
    fig.add_trace(go.Scatter(
        x=dh["year"], y=dh["yield_tonnes"], mode="lines+markers", name="Historical",
        line=dict(color=COLORS["orange"], width=2.5, shape="spline"),
        marker=dict(size=5, color=COLORS["orange"]),
        hovertemplate="%{x}<br>Yield: %{y:.1f} t<extra></extra>",
    ))
    if pd.notna(pred_val):
        fig.add_trace(go.Scatter(
            x=[2025], y=[pred_val], mode="markers", name="2025 Forecast",
            marker=dict(size=16, color=COLORS["green"], symbol="diamond",
                        line=dict(width=2, color=COLORS["surface"])),
            hovertemplate="2025 Forecast<br>%{y:.1f} t<extra></extra>",
        ))
    fig.update_layout(**_layout(
        title=f"{short(district)} — Yield History & 2025 Forecast",
        yaxis=dict(title="Yield (tonnes)", gridcolor=COLORS["grid"]),
        xaxis=dict(title="Year", gridcolor=COLORS["grid"]),
        legend=dict(orientation="h", y=1.12, x=0.5, xanchor="center"),
        height=400,
    ))
    st.plotly_chart(fig, width="stretch")

    # ── Stage risk gauges ─────────────────────────────────────────────────────
    st.markdown("#### Stage Risk Assessment")
    stages = [
        ("squaring_risk_pct", "Squaring", "Jun 1 – Jul 14", COLORS["blue"]),
        ("flowering_risk_pct", "Flowering ⚠️", "Jul 15 – Aug 31", COLORS["orange"]),
        ("bolling_risk_pct", "Bolling", "Sep 1 – Oct 15", COLORS["green"]),
    ]
    cols = st.columns(3)
    for col, (key, label, doy, color) in zip(cols, stages):
        val = dp[key]
        fig_g = go.Figure(go.Indicator(
            mode="gauge+number", value=val, number=dict(suffix="%", font=dict(size=36, color=COLORS["text"])),
            title=dict(text=f"{label}<br><span style='font-size:0.7em;color:#64748B'>{doy}</span>",
                       font=dict(size=14, color=COLORS["text_muted"])),
            gauge=dict(
                axis=dict(range=[0, 100], tickcolor="#475569", dtick=25),
                bar=dict(color=COLORS["green"] if val < 30 else COLORS["orange"] if val < 60 else COLORS["red"], thickness=0.7),
                bgcolor="#1E293B", borderwidth=0,
                steps=[
                    dict(range=[0, 30], color="rgba(16,185,129,0.12)"),
                    dict(range=[30, 60], color="rgba(245,158,11,0.12)"),
                    dict(range=[60, 100], color="rgba(239,68,68,0.12)"),
                ],
                threshold=dict(line=dict(color=COLORS["red"], width=2), thickness=0.8, value=60),
            ),
        ))
        fig_g.update_layout(paper_bgcolor="rgba(0,0,0,0)", font=dict(color=COLORS["text_muted"]),
                            height=220, margin=dict(l=30, r=30, t=60, b=10))
        col.plotly_chart(fig_g, width="stretch")


# ═══════════════════════════════════════════════════════════════════════════════
#  4 · RISK HEATMAP
# ═══════════════════════════════════════════════════════════════════════════════
def page_risk(predictions):
    st.markdown('<p class="section-title">Stage Risk Heatmap — 2025</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">15 districts × 3 growth stages · sorted by flowering risk (most critical stage)</p>', unsafe_allow_html=True)

    rm = predictions.set_index("region")[["squaring_risk_pct", "flowering_risk_pct", "bolling_risk_pct"]].copy()
    rm.columns = ["Squaring (Jun–Jul)", "Flowering (Jul–Aug)", "Bolling (Sep–Oct)"]
    rm.index = [short(i) for i in rm.index]
    rm = rm.sort_values("Flowering (Jul–Aug)", ascending=False)

    fig = px.imshow(
        rm, color_continuous_scale=[[0, "#064E3B"], [0.3, "#10B981"], [0.6, "#F59E0B"], [1.0, "#EF4444"]],
        zmin=0, zmax=100, text_auto=".0f", aspect="auto",
    )
    fig.update_traces(textfont=dict(size=14, color="#F1F5F9", family="DM Mono"))
    fig.update_layout(**_layout(
        height=580,
        xaxis=dict(side="top", tickfont=dict(size=13, color=COLORS["text"]), title=""),
        yaxis=dict(tickfont=dict(size=12, color=COLORS["text"]), title=""),
        coloraxis_colorbar=dict(title="Risk %", thickness=15, len=0.75),
        title="",
    ))
    st.plotly_chart(fig, width="stretch")

    st.markdown(
        '<div class="warning-box">'
        '⚠️ <strong>Flowering (Jul 15–Aug 31)</strong> is the most critical stage. '
        'High night temperatures during this window cause boll shedding. '
        'Districts with flowering risk > 60 % face significant yield loss risk.'
        '</div>', unsafe_allow_html=True
    )

    # ── Box plots ─────────────────────────────────────────────────────────────
    fig2 = go.Figure()
    for stage, label, color in [
        ("squaring_risk_pct", "Squaring", COLORS["blue"]),
        ("flowering_risk_pct", "Flowering", COLORS["orange"]),
        ("bolling_risk_pct", "Bolling", COLORS["green"]),
    ]:
        fig2.add_trace(go.Box(
            y=predictions[stage], name=label, marker_color=color, line_color=color,
            fillcolor="rgba(0,0,0,0)", boxmean=True,
            hovertemplate="%{y:.0f} %<extra>" + label + "</extra>",
        ))
    fig2.update_layout(**_layout(
        title="Risk Distribution by Stage — All Districts",
        showlegend=False, height=350,
        yaxis=dict(title="Risk %", range=[0, 105], gridcolor=COLORS["grid"]),
    ))
    st.plotly_chart(fig2, width="stretch")


# ═══════════════════════════════════════════════════════════════════════════════
#  5 · MODEL INSIGHTS
# ═══════════════════════════════════════════════════════════════════════════════
def page_model(predictions, cotton, features, best_feature):
    st.markdown('<p class="section-title">Model Insights</p>', unsafe_allow_html=True)
    st.markdown('<p class="section-sub">Structural break analysis, night temperature signal, and model performance</p>', unsafe_allow_html=True)

    # ── Period comparison ─────────────────────────────────────────────────────
    st.markdown("#### 📉 Structural Break Analysis — 2019–2021")
    stable = cotton[cotton["year"] <= 2018]
    disrupted = cotton[(cotton["year"] >= 2019) & (cotton["year"] <= 2021)]
    post = cotton[cotton["year"] >= 2022]

    c1, c2, c3 = st.columns(3)
    c1.metric("2000–2018 Stable", f"{stable['yield_tonnes'].mean():.1f} t", "CV R² = 0.240")
    d_mean = disrupted["yield_tonnes"].mean()
    s_mean = stable["yield_tonnes"].mean()
    c2.metric("2019–2021 Disrupted", f"{d_mean:.1f} t",
              f"{((d_mean - s_mean) / s_mean) * 100:+.1f} % vs stable")
    p_mean = post["yield_tonnes"].mean()
    c3.metric("2022–2024 Recovery", f"{p_mean:.1f} t",
              f"{((p_mean - s_mean) / s_mean) * 100:+.1f} % vs stable")

    # ── Mean yield over time ──────────────────────────────────────────────────
    yearly = cotton.groupby("year")["yield_tonnes"].mean().reset_index()
    fig = go.Figure()
    fig.add_vrect(x0=2018.5, x1=2021.5, fillcolor=COLORS["red"], opacity=0.07, line_width=0,
                  annotation_text="Structural Break 2019–2021", annotation_position="top left",
                  annotation_font=dict(size=10, color=COLORS["red"], family="DM Mono"))
    fig.add_trace(go.Scatter(
        x=yearly["year"], y=yearly["yield_tonnes"],
        fill="tozeroy", fillcolor="rgba(245,158,11,0.08)",
        line=dict(color=COLORS["orange"], width=2.5, shape="spline"),
        mode="lines+markers", marker=dict(size=4, color=COLORS["orange"]),
        name="Mean yield",
        hovertemplate="%{x}<br>Mean: %{y:.1f} t<extra></extra>",
    ))
    fig.update_layout(**_layout(
        title="All-District Mean Yield Over Time", showlegend=False, height=340,
        yaxis=dict(title="Mean Yield (t)", gridcolor=COLORS["grid"]),
        xaxis=dict(title="Year", gridcolor=COLORS["grid"]),
    ))
    st.plotly_chart(fig, width="stretch")

    # ── Night temp scatter ────────────────────────────────────────────────────
    st.markdown("#### 🌡️ Flowering Night Temperature vs Yield Anomaly")
    st.caption(
        "Mean minimum temperature during flowering (DOY 196–243, Jul 15–Aug 31). "
        "High nights cause boll shedding — the dominant weather signal."
    )
    feat_plot = features.copy()
    region_mean = feat_plot.groupby("region")["yield_tonnes"].mean()
    feat_plot["yield_anomaly"] = feat_plot["yield_tonnes"] - feat_plot["region"].map(region_mean)
    feat_plot["district"] = feat_plot["region"].apply(short)

    fig2 = px.scatter(
        feat_plot, x="flowering_temp_min_mean", y="yield_anomaly", color="district",
        trendline="ols", trendline_scope="overall", trendline_color_override=COLORS["red"],
        labels={"flowering_temp_min_mean": "Flowering Mean Night Temp (°C)",
                "yield_anomaly": "Yield Anomaly (t)", "district": "District"},
        hover_data={"flowering_temp_min_mean": ":.1f", "yield_anomaly": ":.1f"},
    )
    fig2.update_traces(marker=dict(size=7, opacity=0.7, line=dict(width=0.5, color="#0A0E1A")))
    fig2.update_layout(**_layout(
        title="Flowering Night Temperature vs Yield Anomaly", height=450,
        legend=dict(font=dict(size=10), itemsizing="constant"),
    ))
    st.plotly_chart(fig2, width="stretch")

    st.markdown(
        '<div class="insight-box">'
        '🔬 <strong>Interpretation:</strong> The negative slope confirms that warmer nights during '
        'flowering reduce yield. This single feature explains the bulk of weather-attributable variance (R² ≈ 0.25 '
        'on the stable 2000–2018 period).'
        '</div>', unsafe_allow_html=True
    )

    # ── Model summary ─────────────────────────────────────────────────────────
    st.markdown("#### 🤖 Model Summary")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
| Property | Value |
|---|---|
| Approach | Nested-CV 1-Feature Ridge |
| Target | `yield_anomaly` |
| Best feature | `{best_feature}` |
| Validation | Leave-One-Year-Out (LOYO) |
| CV R² (full 2000–2021) | 0.070 |
| CV R² (stable 2000–2018) | **0.240** |
| MAE | ~6.1 tonnes |
| Training districts | 11 |
| Excluded | Barda, Bilasuvar, Neftchala, Salyan |
| Stage windows | DOY-based (not month-based) |
        """)
    with c2:
        st.markdown("""
**Why district baseline dominates:**
~70 % of yield variance is explained by *which district*, not weather.
Switching to yield anomaly removes this noise.

**Why 2019–2021 is a structural break:**
COVID-era disruptions and policy changes broke the historical
weather–yield relationship. Removing them improves CV R² from 0.070 → 0.240.

**Why DOY windows matter:**
Month-based windows dilute the signal. The flowering window
(DOY 196–243) isolates the biologically critical boll-setting period.

**Why single feature wins:**
Nested-CV consistently selects one dominant weather signal per fold,
confirming R² ≈ 0.25 is the honest ceiling for weather-only models.
        """)
