import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# --- 1. CONFIG (DARK MODE) ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; width: 320px !important; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA INPUT (SỐ LIỆU TỪ SCREENSHOT) ---
# P&L Data
pnl_data = {
    'Month': ['Jan', 'Feb', 'Mar'],
    'Revenue': [5.896, 4.758, 6.241],
    'Expenses': [10.044, 9.127, 8.655],
    'Net Earning': [-4.148, -4.369, -2.414]
}
df_pnl = pd.DataFrame(pnl_data)

# Cash Flow Data [ĐÃ THÊM LẠI]
cfo_data = {
    'Category': ['Depreciation', 'Net Income', 'Inventory'],
    'Actual (M)': [41.7, -54.1, -6.8],
    'Target (M)': [50.0, -20.0, -4.0]
}
df_cfo = pd.DataFrame(cfo_data)

# Operating Fund
current_fund = 1.898
total_budget = 5.000

# --- 3. SIDEBAR (KHU VỰC DỮ LIỆU) ---
with st.sidebar:
    st.markdown("# 📂 BNM DATA HUB") # Dùng Text/Emoji thay cho ảnh bị lỗi
    st.write("---")
    
    # Operating Fund Status
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
    st.caption(f"VND 1.898.000 available for operations.")
    
    st.write("---")
    
    # Bảng P&L
    st.subheader("📊 P&L Statement (M VND)")
    st.dataframe(df_pnl.style.format(precision=3), hide_index=True)
    
    st.write("---")
    
    # Bảng Cash Flow (Đã fix lỗi thiếu bảng)
    st.subheader("💸 Cash Flow Summary")
    st.dataframe(df_cfo, hide_index=True)

# --- 4. MAIN CONTENT ---
st.title("🚀 BNM FINANCIAL COMMAND CENTER")
st.caption("Coffee Division Operations // M4 Optimized")

# Core Metrics
m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Stable")
m3.metric("Operating Fund", "1.898M", "Critical", delta_color="inverse")

st.write("---")

# Row 2: Charts
col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("Revenue vs Expenses Stream")
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Revenue', line=dict(color='#00CC96', width=4)))
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Expenses', line=dict(color='#EF553B', width=4)))
    fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
    st.plotly_chart(fig_line, use_container_width=True)

with col2:
    st.subheader("Daily Efficiency 🎯")
    # Biểu đồ radar hoặc stats nhỏ
    st.info("Optimization: Tăng cường nhân sự ca sáng 10AM để cải thiện 12% hiệu suất.")
    st.metric("Avg Order Value", "42K VND", "↑ 5%")
    st.metric("Break-even Point", "45 Cups", "Target")

st.warning(f"⚠️ **DANGER:** Ngân quỹ vận hành chỉ còn {current_fund}M. Cần kiểm soát chi phí chặt chẽ.")
