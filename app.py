import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 1. SETUP GIAO DIỆN DARK MODE ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    div.block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA INPUT (THEO SỐ LIỆU SẾP GỬI) ---
pnl_data = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Revenue': [5.896, 4.758, 6.241],
    'Expenses': [10.044, 9.127, 8.655],
    'Net_Income': [-4.148, -4.369, -2.414]
}
df_pnl = pd.DataFrame(pnl_data)

cfo_data = {
    'Category': ['Actual', 'Target'], 
    'Depreciation': [41.7, 50.0],
    'Net Income': [-54.1, -20.0],
    'Inventory': [-6.8, -4.0]
}
df_cfo = pd.DataFrame(cfo_data)

# --- 3. SIDEBAR (BẢNG SỐ CHI TIẾT) ---
with st.sidebar:
    st.title("📂 BNM DATA")
    st.write("**Profit & Loss (M VND)**")
    st.dataframe(df_pnl, hide_index=True)
    st.write("---")
    st.write("**Cash Flow Analysis**")
    st.dataframe(df_cfo, hide_index=True)
    st.write("---")
    st.caption("M4 Optimized // 2026 Edition")

# --- 4. GIAO DIỆN CHÍNH ---
st.header("FINANCIAL REPORT COMMAND CENTER")
st.caption("Coffee Division // BNM Project Strategy")

# Row 1: Key Metrics
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Operational Burn Rate", "6.8M VND", "Avg")
m3.metric("Cash Runway (Target)", "5.1 Months", "🎯 Target")

st.write("---")

# Row 2: Charts (Chia 2 cột y chang ảnh)
col_left, col_right = st.columns([1.2, 1])

with col_left:
    # Biểu đồ đường Revenue & Expenses
    st.subheader("Revenue Stream Convergence")
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Net Revenue', line=dict(color='#00CC96', width=3)))
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Total Expenses', line=dict(color='#EF553B', width=3)))
    fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(l=0,r=0,b=0,t=20))
    st.plotly_chart(fig_line, use_container_width=True)

    # Biểu đồ cột Stacked Bar Actual vs Target
    st.subheader("Actual vs Target Breakdown")
    fig_bar = px.bar(df_cfo, x='Category', y=['Depreciation', 'Net Income', 'Inventory'],
                     color_discrete_map={'Depreciation': '#00CC96', 'Net Income': '#EF553B', 'Inventory': '#FECB52'},
                     barmode='relative', template="plotly_dark")
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(l=0,r=0,b=0,t=20))
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    # Biểu đồ 3D "Gai Góc" (Rock Edition)
    st.subheader("[02] OPERATIONS_EFFICIENCY")
    x = np.linspace(-5, 5, 80)
    y = np.linspace(-5, 5, 80)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X) * np.cos(Y) + np.sin(np.sqrt(X**2 + Y**2))
    Z += np.random.normal(0, 0.25, X.shape) # Tạo gai nhọn
    
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Greys', showscale=False)])
    fig_3d.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False), 
                        margin=dict(l=0, r=0, b=0, t=0), height=720, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_3d, use_container_width=True)

st.markdown("---")
st.info("💡 **INSIGHT:** Tăng cường tối ưu Inventory tháng 4 để kéo Cash Runway lên 6 tháng.")
