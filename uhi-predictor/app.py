# Main Streamlit Application UI

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import requests
import time
import os
from config import CITIES, SEVERITY_COLORS
from pipeline import MODEL_PATH, predict_uhi

st.set_page_config(
    page_title="UHI Predictor — India",
    page_icon="🌡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
/* Hide Streamlit default elements */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main background */
.stApp {
    background-color: #f8fafc;
}

/* Sidebar styling */
[data-testid="stSidebar"] {
    background-color: #ffffff;
    border-right: 1px solid #e2e8f0;
}

/* Metric cards */
[data-testid="stMetric"] {
    background-color: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 10px;
    padding: 16px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}

[data-testid="stMetricLabel"] {
    color: #64748b !important;
    font-size: 12px !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

[data-testid="stMetricValue"] {
    color: #0f172a !important;
    font-size: 28px !important;
    font-weight: 600 !important;
}

/* Tab styling */
[data-testid="stTabs"] button {
    color: #64748b;
    font-weight: 500;
    font-size: 14px;
}

[data-testid="stTabs"] button[aria-selected="true"] {
    color: #0f172a;
    border-bottom-color: #3b82f6;
}

/* Buttons */
[data-testid="stButton"] button {
    border-radius: 8px;
    font-weight: 600;
    letter-spacing: 0.02em;
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
}

/* Divider */
hr {
    border-color: #e2e8f0;
}

/* Spinner */
[data-testid="stSpinner"] {
    color: #3b82f6;
}
</style>
""", unsafe_allow_html=True)

if "map_data" not in st.session_state:
    st.session_state.map_data = []

st.markdown("""
<div style="padding: 24px 0 8px 0;">
    <div style="display:flex; align-items:center; gap:12px; margin-bottom:6px;">
        <span style="font-size:36px;">🌡️</span>
        <div>
            <h1 style="margin:0; font-size:28px; font-weight:700; color:#0f172a; 
                        letter-spacing:-0.02em;">Urban Heat Island Predictor</h1>
            <p style="margin:0; font-size:13px; color:#475569;">
                India · Live AI analysis · Powered by Open-Meteo API + XGBoost ML
            </p>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

if os.path.exists(MODEL_PATH):
    st.markdown("""
    <div style="background:#f0fdf4; border:1px solid #22c55e; border-radius:8px; 
                padding:8px 16px; display:inline-block; margin-bottom:12px;">
        <span style="color:#15803d; font-size:13px; font-weight:600;">
            ● ML Model Active — XGBoost classifier loaded
        </span>
    </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
    <div style="background:#fef2f2; border:1px solid #ef4444; border-radius:8px; 
                padding:8px 16px; display:inline-block; margin-bottom:12px;">
        <span style="color:#b91c1c; font-size:13px; font-weight:600;">
            ● ML Model Offline — App will not predict!
        </span>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div style="padding:16px 0 8px 0; border-bottom:1px solid #e2e8f0; margin-bottom:16px;">
        <p style="color:#0f172a; font-size:16px; font-weight:600; margin:0;">UHI Predictor</p>
        <p style="color:#64748b; font-size:11px; margin:0;">Urban Heat Island Monitor · India</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<p style="color:#64748b; font-size:11px; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:8px;">Select City</p>', unsafe_allow_html=True)
    selected_city = st.selectbox("Select City", options=list(CITIES.keys()), label_visibility="collapsed")
    predict_btn = st.button("Predict UHI →", type="primary", use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown('<p style="color:#64748b; font-size:11px; text-transform:uppercase; letter-spacing:0.08em; margin-bottom:8px;">Severity Scale</p>', unsafe_allow_html=True)
    severity_info = {
        "None":     ("#06b6d4", "No thermal anomaly"),
        "Mild":     ("#22c55e", "ML detecting emerging UHI"),
        "Moderate": ("#f59e0b", "Strong algorithmic confidence"),
        "Severe":   ("#dc2626", "Critical heat identified by Model"),
    }
    for level, (color, desc) in severity_info.items():
        st.markdown(f"""
        <div style="display:flex; align-items:center; gap:8px; margin-bottom:6px;">
            <div style="width:10px; height:10px; border-radius:50%; background:{color}; flex-shrink:0;"></div>
            <div>
                <span style="color:#0f172a; font-size:12px; font-weight:600;">{level}</span>
                <span style="color:#475569; font-size:11px;"> — {desc}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background:#f1f5f9; border-radius:8px; padding:10px 12px; 
                border:1px solid #e2e8f0;">
        <p style="color:#475569; font-size:11px; text-transform:uppercase; 
                   letter-spacing:0.08em; margin:0 0 4px 0; font-weight:600;">What is UHI?</p>
        <p style="color:#64748b; font-size:11px; margin:0; line-height:1.5;">
            Urban areas are significantly hotter than surrounding rural areas 
            due to concrete, reduced greenery, and human activity.
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<p style="color:#94a3b8; font-size:10px;">Live data: Open-Meteo API<br>Model: XGBoost Classifier<br>Team Tech Titans 2026</p>', unsafe_allow_html=True)

@st.cache_data(ttl=3600*24)
def fetch_india_geojson():
    url = "https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson"
    r = requests.get(url)
    return r.json()

tab1, tab2 = st.tabs(["🌍 India Live Map", "🏢 Single City Result"])

with tab1:
    col_h, col_btn = st.columns([4, 1])
    with col_h:
        st.markdown("""
        <h3 style="color:#0f172a; margin:0; font-size:18px; font-weight:600;">
            India Live UHI Heatmap
        </h3>
        <p style="color:#64748b; font-size:12px; margin:4px 0 12px 0;">
            Choropleth map with strict state-boundary masking
        </p>
        """, unsafe_allow_html=True)
    with col_btn:
        load_btn = st.button("Load map →", type="primary", use_container_width=True)

    if load_btn:
        progress = st.progress(0, text="Initialising...")
        
        progress.progress(20, text="Fetching live city data...")
        all_cities_data = []
        for i, city in enumerate(CITIES.keys()):
            res = predict_uhi(city)
            if res is not None:
                lat, lon = CITIES[city]["urban"]
                res["lat"] = lat
                res["lon"] = lon
                all_cities_data.append(res)
            import time
            time.sleep(0.5) # Prevent Open-Meteo rate limiting which drops cities!
            progress.progress(20 + int((i/len(CITIES))*80), text=f"Processing {city}...")
        
        progress.progress(100, text="Done!")
        progress.empty()
        
        st.session_state.map_data = all_cities_data
        
    if st.session_state.map_data:
        all_cities_data = st.session_state.map_data
        
        # Summary stats
        severe_count = len([r for r in all_cities_data if r["severity"] == "Severe"])
        max_uhi = max(all_cities_data, key=lambda x: x["uhi_intensity"])
        min_uhi = min(all_cities_data, key=lambda x: x["uhi_intensity"])
        avg_uhi = sum(r["uhi_intensity"] for r in all_cities_data) / len(all_cities_data)
        
        st.markdown("<br>", unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns(4)
        c1.metric("Cities at severe risk", severe_count)
        c2.metric("Highest UHI", f"+{max_uhi['uhi_intensity']}°C", max_uhi['city'])
        c3.metric("Lowest UHI", f"+{min_uhi['uhi_intensity']}°C", min_uhi['city'])
        c4.metric("Average UHI", f"+{avg_uhi:.1f}°C", "across all cities")
        st.markdown("<br>", unsafe_allow_html=True)
        
        geojson_data = fetch_india_geojson()
        df = pd.DataFrame(all_cities_data)
        df["State"] = [CITIES[c]["State"] for c in df["city"]]

        fig = go.Figure()
        
        # Add the State Choropleth Heatmap (Zero Ocean Bleed!)
        fig.add_trace(go.Choroplethmapbox(
            geojson=geojson_data,
            locations=df["State"],
            featureidkey="properties.ST_NM",
            z=df["uhi_intensity"],
            colorscale=[[0.0, "rgba(6,182,212,0.3)"], [0.25, "rgba(34,197,94,0.4)"], [0.5, "rgba(245,158,11,0.5)"], [1.0, "rgba(220,38,38,0.7)"]],
            zmin=0, zmax=5,
            marker_opacity=1.0,
            marker_line_width=1,
            marker_line_color="#1e293b",
            hoverinfo="location+z",
            hovertemplate="<b>%{location}</b><br>State UHI: +%{z:.1f}°C<extra></extra>",
            showscale=False
        ))
        
        # Add the Cities as exact glowing points on top
        fig.add_trace(go.Scattermapbox(
            lat=df["lat"],
            lon=df["lon"],
            mode="markers+text",
            text=df["city"],
            textposition="top right",
            textfont=dict(color="#0f172a", size=11),
            marker=dict(
                size=12,
                color=df["color"]
            ),
            hovertext=df.apply(lambda x: f"<b>{x['city']}</b><br>Urban: {x['urban_temp']}°C<br>Rural: {x['rural_temp']}°C<br>UHI: +{x['uhi_intensity']}°C<br>Severity: {x['severity']}", axis=1),
            hoverinfo="text",
        ))
        
        fig.update_layout(
            mapbox=dict(
                style="carto-positron",
                center=dict(lat=22, lon=82),
                zoom=3.8,
                accesstoken=None
            ),
            height=560,
            margin=dict(r=0, t=0, l=0, b=0),
            paper_bgcolor="#f8fafc",
            font_color="#334155",
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        
        st.subheader("City Data")
        display_df = df[["city", "urban_temp", "rural_temp", "uhi_intensity", "severity", "color"]].copy()
        
        st.dataframe(
            display_df[["city", "urban_temp", "rural_temp", "uhi_intensity", "severity"]],
            use_container_width=True,
            hide_index=True,
            column_config={
                "city": "City",
                "urban_temp": st.column_config.NumberColumn(
                    "Urban Temp (°C)",
                    format="%.1f °C",
                ),
                "rural_temp": st.column_config.NumberColumn(
                    "Rural Temp (°C)",
                    format="%.1f °C",
                ),
                "uhi_intensity": st.column_config.NumberColumn(
                    "UHI Intensity (°C)",
                    format="%.1f °C",
                ),
                "severity": "Severity",
            }
        )

with tab2:
    if predict_btn:
        with st.spinner(f"Fetching live data and predicting UHI for {selected_city}..."):
            res = predict_uhi(selected_city)
            
            if res is None:
                st.error("Failed to fetch live data from the API. Please try again later.")
            else:
                col1, col2, col3, col4, col5 = st.columns(5)
                col1.metric("Urban Temp", f"{res['urban_temp']} °C")
                col2.metric("Rural Temp", f"{res['rural_temp']} °C")
                diff = res['uhi_intensity']
                col3.metric("UHI Intensity", f"{diff} °C", f"{diff} (difference)" if diff > 0 else "")
                col4.metric("Humidity", f"{res['humidity']} %")
                col5.metric("Wind Speed", f"{res.get('wind', 'N/A')} km/h")
                
                st.markdown(f"""
                <div style="background: linear-gradient(135deg, {res['color']}22, {res['color']}44);
                            border: 2px solid {res['color']};
                            border-radius: 14px;
                            padding: 28px 20px;
                            text-align: center;
                            margin: 16px 0;
                            box-shadow: 0 0 30px {res['color']}33;">
                    <p style="color:{res['color']}; font-size:11px; font-weight:600; 
                               text-transform:uppercase; letter-spacing:0.15em; margin:0 0 8px 0;">
                        UHI Severity Level
                    </p>
                    <p style="color:{res['color']}; font-size:52px; font-weight:700; 
                               margin:0 0 8px 0; line-height:1;">
                        {res['severity'].upper()}
                    </p>
                    <p style="color:#64748b; font-size:13px; margin:0;">
                        {selected_city} urban area is 
                        <span style="color:{res['color']}; font-weight:600;">
                            +{res['uhi_intensity']}°C
                        </span> 
                        hotter than surrounding rural area
                    </p>
                </div>
                """, unsafe_allow_html=True)
                
                if res["severity"] == "Severe":
                    st.error("Health Advisory: Extreme heat conditions. Vulnerable populations should stay indoors. High risk of heatstroke.")
                elif res["severity"] == "Moderate":
                    st.warning("Health Advisory: Significant heat differences detected. Ensure adequate hydration and limit outdoor exertion.")
                elif res["severity"] == "Mild":
                    st.info("Health Advisory: Mild heat island effect. Conditions are generally manageable, but stay mindful of hydration.")
                else:
                    st.success("Health Advisory: Favorable thermal conditions. No significant heat concerns.")
                
                if st.session_state.map_data:
                    with st.expander("Compare with other cities", expanded=True):
                        comp_df = pd.DataFrame(st.session_state.map_data)[["city","uhi_intensity","color"]]
                        comp_df = comp_df.sort_values("uhi_intensity", ascending=True)
                        
                        opacities = [1.0 if c == selected_city else 0.5 for c in comp_df["city"]]
                        
                        fig_bar = go.Figure(go.Bar(
                            x=comp_df["uhi_intensity"],
                            y=comp_df["city"],
                            orientation='h',
                            marker_color=comp_df["color"],
                            marker=dict(opacity=opacities),
                            text=comp_df["uhi_intensity"].apply(lambda x: f"+{x}°C"),
                            textposition='outside',
                            textfont=dict(color='#0f172a')
                        ))
                        
                        fig_bar.update_layout(
                            title=f"UHI intensity comparison — {selected_city} highlighted",
                            title_font=dict(color="#0f172a"),
                            paper_bgcolor="#f8fafc",
                            plot_bgcolor="#f8fafc",
                            font_color="#475569",
                            margin=dict(l=0, r=0, t=40, b=0),
                            height=400,
                            xaxis=dict(showgrid=True, gridcolor="#e2e8f0", title="UHI Intensity (°C)"),
                            yaxis=dict(title="")
                        )
                        st.plotly_chart(fig_bar, use_container_width=True)
                
                with st.expander("Technical details"):
                    from config import FEATURE_COLUMNS
                    st.write(f"**ML Model Used:** {'Yes (XGBoost)' if res['using_ml_model'] else 'No (Rule-based Fallback)'}")
                    st.write("**Feature Vector Matrix:**")
                    feature_dict = dict(zip(FEATURE_COLUMNS, res['features']))
                    st.json(feature_dict)
                    
                    import math
                    # Create a horizontal bar chart to visualize the feature matrix with a log axis
                    fig_features = go.Figure(go.Bar(
                        x=list(feature_dict.values()),
                        y=list(feature_dict.keys()),
                        orientation='h',
                        marker=dict(
                            color="rgba(6, 182, 212, 0.6)", # Cyan with opacity
                            line=dict(color="#06b6d4", width=1)
                        ),
                        text=[f"{v:g}" for v in feature_dict.values()],
                        textposition="outside",
                        textfont=dict(color="#0f172a")
                    ))
                    
                    fig_features.update_layout(
                        title="Feature Distribution Analyzer (Log Scale View)",
                        title_font=dict(color="#0f172a", size=14),
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        font_color="#475569",
                        height=350,
                        margin=dict(l=0, r=30, t=40, b=0), # Add right margin so text doesn't explicitly clip
                        xaxis=dict(type="log", title="Values (Logarithmic)", gridcolor="#e2e8f0"),
                        yaxis=dict(title="")
                    )
                    st.plotly_chart(fig_features, use_container_width=True)

    elif not predict_btn:
        st.info("Select a city from the sidebar and click 'Predict UHI' to see results.")

st.markdown("""
<div style="border-top:1px solid #e2e8f0; padding:16px 0; margin-top:24px;">
    <p style="color:#64748b; font-size:11px; text-align:center; margin:0;">
        Live data: Open-Meteo API (non-commercial) · 
        Training: Kaggle UHI Monitoring Dataset · 
        Model: XGBoost Classifier · 
        Team Tech Titans · April 2026
    </p>
</div>
""", unsafe_allow_html=True)
