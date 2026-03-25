import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from pyngrok import ngrok
import logging
import warnings

# --- KHÂU MỎ TERMINAL (TẮT CẢNH BÁO RÁC) ---
warnings.filterwarnings("ignore")
logging.getLogger('streamlit.runtime.scriptrunner.script_run_context').setLevel(logging.ERROR)

# --- 1. CONFIG NGROK ---
NGROK_AUTH_TOKEN = "3BMw0F0iFZWMfix8B979mAzXXj9_7WXNREb7fDAQzT3KByhkC"
@st.cache_resource
def setup_ngrok():
    try:
        ngrok.set_auth_token(NGROK_AUTH_TOKEN)
        return ngrok.connect(8501).public_url
    except: return "Lỗi Ngrok"

public_url = setup_ngrok()

# --- 2. GIAO DIỆN DARK MODE ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    div.block-container { padding-top: 2rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 3. DỮ LIỆU THỰC TẾ ---
data = {
    'Month': ['January', 'February', 'March'],
    'Revenue': [5.896, 4.758, 6.241],
    'Net_Income': [-4.148, -4.369, -2.414]
}
df = pd.DataFrame(data)

# --- 4. SIDEBAR ---
with st.sidebar:
    st.title("🛡️ BNM CONTROL")
    st.dataframe(df) # Đã xóa thuộc tính gây lỗi
    st.success(f"🌐 **Tommy's Link:** \n\n {public_url}")

# --- 5. GIAO DIỆN CHÍNH ---
st.title("📊 BROKENOMORE (BNM) FINANCIAL COMMAND CENTER")

m1, m2, m3 = st.columns(3)
with m1: st.metric("Gross Margin", "41.4%", "2.1%")
with m2: st.metric("Burn Rate (Avg)", "5.2M VND", "-15%")
with m3: st.metric("Cash Runway", "5.1 Months", "Target")

left_col, right_col = st.columns([2, 1])

with left_col:
    fig_line = px.line(df, x='Month', y=['Revenue', 'Net_Income'], markers=True,
                       color_discrete_map={"Revenue": "#00CC96", "Net_Income": "#EF553B"},
                       template="plotly_dark")
    st.plotly_chart(fig_line, width="stretch") # Đã dùng width="stretch" chuẩn 2026

with right_col:
    x, y = np.linspace(-2, 2, 30), np.linspace(-2, 2, 30)
    X, Y = np.meshgrid(x, y)
    Z = np.exp(-(X**2 + Y**2))
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis', showscale=False)])
    fig_3d.update_layout(margin=dict(l=0, r=0, b=0, t=0), height=350, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_3d, width="stretch") # Đã dùng width="stretch" chuẩn 2026
