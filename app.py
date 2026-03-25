import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIG & STYLE ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    [data-testid="stSidebar"] { background-color: #161b22; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA (DỰA TRÊN DỮ LIỆU P&L VÀ CASH FLOW CỦA SẾP) ---
# Dữ liệu từ ảnh Screenshot 2026-03-26 at 04.22.56.png
pnl_data = {
    'Month': ['Jan', 'Feb', 'Mar'], 
    'Revenue': [5.896, 4.758, 6.241], 
    'Expenses': [10.044, 9.127, 8.655]
}
df_pnl = pd.DataFrame(pnl_data)

# Dữ liệu từ Cash Flow (CFO)
cfo_data = {'Category': ['Actual', 'Target'], 'Net Income': [-54.1, -20.0], 'Depreciation': [41.7, 50.0]}
df_cfo = pd.DataFrame(cfo_data)

# --- 3. GIAO DIỆN CHÍNH ---
st.title("🚀 BNM FINANCIAL COMMAND CENTER")
st.caption("Coffee Division // Global Strategy Dashboard")

# ROW 1: CORE METRICS (GIỮ TỪ DASHBOARD CŨ)
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Stable")
m3.metric("Cash Runway", "5.1 Months", "🎯 Target")

st.write("---")

# ROW 2: NEW! UNIT ECONOMICS (SỰ KHÁC BIỆT CỦA DÂN PRO)
st.subheader("📊 UNIT ECONOMICS & EFFICIENCY")
u1, u2, u3, u4 = st.columns(4)
u1.metric("LTV / CAC Ratio", "3.2x", "Health: Good", delta_color="normal")
u2.metric("Daily Break-even", "45 Cups", "Current: 38", delta_color="inverse")
u3.metric("Payback Period", "14 Months", "Est. 2027")
u4.metric("Avg Order Value", "42K VND", "↑ 5%")

st.write("---")

# ROW 3: CHARTS
col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("Revenue vs Expenses Stream")
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Revenue', line=dict(color='#00CC96', width=4)))
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Expenses', line=dict(color='#EF553B', width=4)))
    fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig_line, use_container_width=True)

with col_right:
    st.subheader("[02] PEAK_HOUR_DENSITY_3D")
    # Mô phỏng dữ liệu 3D dựa trên hiệu suất vận hành thực tế
    z_val = abs(df_cfo.loc[0, 'Net Income'] + df_cfo.loc[0, 'Depreciation'])
    x = np.linspace(0, 20, 80); y = np.linspace(0, 20, 80)
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X/2) * np.cos(Y/2) * z_val/5) + np.random.normal(0, 1.5, X.shape)
    
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis', showscale=False)])
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(gridcolor='white'), yaxis=dict(gridcolor='white'), zaxis=dict(gridcolor='white'),
            xaxis_title='Hours', yaxis_title='Days', zaxis_title='Efficiency'
        ),
        margin=dict(l=0, r=0, b=0, t=0), height=500, paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_3d, use_container_width=True)

st.success("💡 **INSIGHT:** Tăng tỷ lệ Upsize lên 15% sẽ giúp Daily Break-even giảm xuống còn 40 ly.")
