import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIG GIAO DIỆN ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; width: 320px !important; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    div.block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DỮ LIỆU TỔNG HỢP ---
pnl_data = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Revenue': [5.896, 4.758, 6.241],
    'Expenses': [10.044, 9.127, 8.655],
    'Net Earning': [-4.148, -4.369, -2.414]
}
df_pnl = pd.DataFrame(pnl_data)

cfo_data = {
    'Category': ['Depreciation', 'Net Income', 'Inventory'],
    'Actual (M)': [41.7, -54.1, -6.8],
    'Target (M)': [50.0, -20.0, -4.0]
}
df_cfo = pd.DataFrame(cfo_data)

current_fund = 1.898
total_budget = 5.000

# --- 3. SIDEBAR (DỮ LIỆU & QUỸ) ---
with st.sidebar:
    st.markdown("# Excel Data")
    st.write("---")
    
    st.subheader("💳 Operating Fund Status")
    fig_fund = go.Figure(go.Pie(
        labels=['Remaining', 'Used'],
        values=[current_fund, total_budget - current_fund],
        hole=.7,
        marker_colors=['#00CC96', '#30363d'],
        textinfo='none'
    ))
    fig_fund.update_layout(
        showlegend=False, height=180, margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor='rgba(0,0,0,0)',
        annotations=[dict(text=f'{current_fund}M', x=0.5, y=0.5, font_size=20, showarrow=False, font_color="white")]
    )
    st.plotly_chart(fig_fund, use_container_width=True)
    
    st.write("---")
    st.subheader("📊 P&L Statement")
    st.dataframe(df_pnl.style.format(precision=3), hide_index=True)
    
    st.write("---")
    st.subheader("💸 Cash Flow Summary")
    st.dataframe(df_cfo, hide_index=True)

# --- 4. MAIN CONTENT ---
st.header("Financial Report")
st.caption("Strategy Optimization")

# ROW 1: CORE METRICS
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Stable")
m3.metric("Operating Fund", "1.898M", "-3.1M vs Initial", delta_color="inverse")

st.write("---")

# ROW 2: UNIT ECONOMICS (CÁI NÀY NÃY BỊ MẤT NÈ)
st.subheader("📊 Unit Economics Analysis")
u1, u2, u3, u4 = st.columns(4)
u1.metric("LTV / CAC Ratio", "3.2x", "Health: Good")
u2.metric("Daily Break-even", "45 Cups", "🎯 Target")
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
    st.subheader("PEAK HOUR 3D")
    # Biểu đồ 3D gai góc có Grid
    x = np.linspace(0, 24, 50); y = np.linspace(0, 7, 50)
    X, Y = np.meshgrid(x, y)
    Z = (np.sin(X/3) * np.cos(Y/2) * 5) + np.random.normal(0, 1.1, X.shape)
    
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis', showscale=False)])
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(title='Hours', gridcolor='white'),
            yaxis=dict(title='Days', gridcolor='white'),
            zaxis=dict(title='Efficiency', gridcolor='white'),
        ),
        margin=dict(l=0, r=0, b=0, t=0), height=500, paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_3d, use_container_width=True)

st.warning(f"💡 **STRATEGY:** Cần đẩy mạnh Upsize và Combo để tối ưu hóa Avg Order Value trong tháng 4.")
