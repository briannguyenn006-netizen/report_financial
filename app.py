import streamlit as st
import pandas as pd
import plotly.express as px
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

# --- 2. DỮ LIỆU THỰC TẾ ---
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

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("📂 DATA INPUT")
    st.subheader("LIVE DATA FROM EXCEL")
    st.write("**P&L (M VND)**")
    st.dataframe(df_pnl, hide_index=True)
    st.write("---")
    st.write("**Cash Flow (M VND)**")
    st.dataframe(df_cfo, hide_index=True)
    st.write("---")
    st.caption("M4 Optimized // BNM Finance Lab")

# --- 4. GIAO DIỆN CHÍNH ---
st.header("BROKENOMORE (BNM) FINANCIAL COMMAND CENTER")
st.caption("Coffee Division Operations // PEAK_HOUR_DENSITY_3D optimization")

m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin (Mar)", "41.4%", "↑ 2.1%")
m2.metric("Operational Burn Rate", "6.8M VND", "Avg")
m3.metric("Cash Runway (Target)", "5.1 Months", "🎯 Target")

st.write("---")

col_left, col_right = st.columns([1.2, 1])

with col_left:
    st.subheader("Revenue Stream Convergence")
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Total Net Revenue', line=dict(color='#00CC96', width=3)))
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Total Expenses', line=dict(color='#EF553B', width=3)))
    fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350)
    st.plotly_chart(fig_line, use_container_width=True)

    st.subheader("Actual vs Target Cash Flow")
    fig_bar = px.bar(df_cfo, x='Category', y=['Depreciation', 'Net Income', 'Inventory'],
                     color_discrete_map={'Depreciation': '#00CC96', 'Net Income': '#EF553B', 'Inventory': '#FECB52'},
                     barmode='relative', template="plotly_dark")
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("[02] OPERATIONS_EFFICIENCY")
    # TÁI TẠO ĐỘ GAI GÓC NHƯ HÌNH THAM KHẢO
    x = np.linspace(0, 20, 80) # Tăng mật độ lên 80 để gai cực nhọn
    y = np.linspace(0, 20, 80)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(X/2) * np.cos(Y/2) + np.sin(np.sqrt(X**2 + Y**2))
    Z += np.random.normal(0, 0.25, X.shape) # Noise mạnh tạo độ răng cưa
    
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Greys', showscale=False)])
    fig_3d.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False), 
                        margin=dict(l=0, r=0, b=0, t=0), height=700, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_3d, use_container_width=True)

st.info("💡 **OPTIMIZATION OPPORTUNITY:** Adjust Mar 10am shift +1 staff for 12% projected efficiency gain.")
