import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1. CONFIG ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide")
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 10px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DỮ LIỆU ---
pnl_data = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Revenue': [5.896, 4.758, 6.241],
    'Expenses': [10.044, 9.127, 8.655],
    'Net Earning': [-4.148, -4.369, -2.414]
}
df_pnl = pd.DataFrame(pnl_data)

# Số liệu Operating Fund từ sếp gửi
current_fund = 1.898
total_budget = 5.000 # Giả định tổng ngân sách ban đầu để vẽ biểu đồ tròn

# --- 3. SIDEBAR: DATA & OPERATING FUND ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/money-bag-v1.png", width=50)
    st.title("📂 BNM DATA HUB")
    
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
    
    st.subheader("📊 P&L Statement (M VND)")
    st.dataframe(df_pnl.style.format(precision=3), hide_index=True)

# --- 4. MAIN DASHBOARD ---
st.title("🚀 BNM FINANCIAL COMMAND CENTER")
st.caption("Coffee Division Operations // Strategy Optimization")

# Metrics chính
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Stable")
m3.metric("Operating Fund", "1.898M", "Critical", delta_color="inverse")

st.write("---")

# Hàng 2: Unit Economics
u1, u2, u3, u4 = st.columns(4)
u1.metric("LTV / CAC Ratio", "3.2x", "Health: Good")
u2.metric("Daily Break-even", "45 Cups", "Target")
u3.metric("Payback Period", "14 Months", "Est. 2027")
u4.metric("Avg Order Value", "42K VND", "↑ 5%")

st.write("---")

# Hàng 3: Revenue Stream Chart
st.subheader("Revenue vs Expenses Stream")
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Revenue', line=dict(color='#00CC96', width=4)))
fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Expenses', line=dict(color='#EF553B', width=4)))
fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
st.plotly_chart(fig_line, use_container_width=True)

st.warning(f"⚠️ **ALERT:** Với Operating Fund hiện tại ({current_fund}M), sếp cần tối ưu hóa dòng tiền tháng 4 để duy trì Runway.")
