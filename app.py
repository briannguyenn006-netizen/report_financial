import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIG GIAO DIỆN DARK MODE ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.block-container { padding-top: 2rem; }
    .stMetric { background-color: #161b22; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DỮ LIỆU THỰC TẾ ---
data = {
    'Month': ['January', 'February', 'March'],
    'Revenue': [5.896, 4.758, 6.241],
    'Net_Income': [-4.148, -4.369, -2.414]
}
df = pd.DataFrame(data)

# --- 3. GIAO DIỆN CHÍNH ---
st.title("📊 BNM FINANCIAL COMMAND CENTER")
st.sidebar.title("🛡️ BNM CONTROL")
st.sidebar.dataframe(df)

m1, m2, m3 = st.columns(3)
with m1: st.metric("Gross Margin", "41.4%", "2.1%")
with m2: st.metric("Burn Rate (Avg)", "5.2M VND", "-15%")
with m3: st.metric("Cash Runway", "5.1 Months", "Target")

left_col, right_col = st.columns([2, 1])

with left_col:
    fig_line = px.line(df, x='Month', y=['Revenue', 'Net_Income'], markers=True,
                       color_discrete_map={"Revenue": "#00CC96", "Net_Income": "#EF553B"},
                       template="plotly_dark")
    st.plotly_chart(fig_line, use_container_width=True)

with right_col:
    x, y = np.linspace(-2, 2, 30), np.linspace(-2, 2, 30)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis', showscale=False)])
    fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), height=350, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_3d, use_container_width=True)
