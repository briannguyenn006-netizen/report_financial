import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIG GIAO DIỆN (DARK MODE M4 OPTIMIZED) ---
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
    'Net Earning': [-4.148, -4.369, -2.414]
}
df_pnl = pd.DataFrame(pnl_data)

cfo_data = {
    'Category': ['Actual', 'Target'], 
    'Depreciation': [41.7, 50.0],
    'Net Income': [-54.1, -20.0],
    'Inventory': [-6.8, -4.0]
}
df_cfo = pd.DataFrame(cfo_data)

# Số liệu Operating Fund từ sếp gửi
current_fund = 1.898
total_budget = 5.000 # Giả định tổng ngân sách ban đầu

# --- 3. SIDEBAR (BẢNG SỐ LIỆU LIVE BÊN TRÁI) ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/money-bag-v1.png", width=50) # --- ĐÃ FIX: ICON MÀU MÈ ---
    st.title("📂 BNM DATA HUB")
    st.write("---")
    
    # Biểu đồ Ngân sách còn lại (Operating Fund)
    st.subheader("💳 Operating Fund Status")
    fig_fund = go.Figure(go.Pie(
        labels=['Remaining', 'Used'],
        values=[current_fund, total_budget - current_fund],
        hole=.7,
        marker_colors=['#00CC96', '#30363d'],
        textinfo='none'
    ))
    fig_fund.update_layout(
        showlegend=False, height=200, margin=dict(t=0, b=0, l=0, r=0),
        paper_bgcolor='rgba(0,0,0,0)',
        annotations=[dict(text=f'{current_fund}M', x=0.5, y=0.5, font_size=20, showarrow=False, font_color="white")]
    )
    st.plotly_chart(fig_fund, use_container_width=True)
    st.caption(f"VND 1.898.000 available for operations.")
    
    st.write("---")
    
    # --- ĐÃ FIX: CHÈN BẢNG P&L ---
    st.subheader("📊 P&L Statement (M VND)")
    st.dataframe(df_pnl.style.format(precision=3), hide_index=True)
    
    st.write("---")
    
    # --- ĐÃ FIX: CHÈN BẢNG CASHFLOW ---
    st.subheader("💸 Cash Flow Summary (M VND)")
    st.dataframe(df_cfo, hide_index=True)
    st.write("---")
    st.caption("M4 Optimized // 2026 Edition")

# --- 4. GIAO DIỆN CHÍNH (COMMAND CENTER) ---
st.header("BROKENOMORE (BNM) FINANCIAL COMMAND CENTER")
st.caption("Coffee Division Operations // Monthly Target Overview")

# Row 1: Core Metrics
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Stable")
m3.metric("Operating Fund", "1.898M", "Critical", delta_color="inverse")

st.write("---")

# Row 2: Unit Economics
st.subheader("📊 Unit Economics Analysis")
u1, u2, u3, u4 = st.columns(4)
u1.metric("LTV / CAC Ratio", "3.2x", "Health: Good")
u2.metric("Daily Break-even", "45 Cups", "🎯 Target")
u3.metric("Payback Period", "14 Months", "Est. 2027")
u4.metric("Avg Order Value", "42K VND", "↑ 5%")

st.write("---")

# Row 3: Revenue Stream Chart
st.subheader("Revenue vs Expenses Stream")
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Revenue', line=dict(color='#00CC96', width=4)))
fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Expenses', line=dict(color='#EF553B', width=4)))
fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=450)
st.plotly_chart(fig_line, use_container_width=True)

st.warning(f"⚠️ **ALERT:** Operating Fund thấp. Cần ưu tiên tối ưu COGS tháng 4.")
