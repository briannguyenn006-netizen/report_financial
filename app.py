import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 1. SETTING GIAO DIỆN ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    div.block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA CHUẨN (NHƯ TRONG SCREENSHOT) ---
pnl_data = {'Month': ['Jan', 'Feb', 'Mar'], 'Revenue': [5.896, 4.758, 6.241], 'Expenses': [10.044, 9.127, 8.655]}
df_pnl = pd.DataFrame(pnl_data)

cfo_data = {'Category': ['Actual', 'Target'], 'Depreciation': [41.7, 50.0], 'Net Income': [-54.1, -20.0], 'Inventory': [-6.8, -4.0]}
df_cfo = pd.DataFrame(cfo_data)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("📂 DATA INPUT")
    st.write("**P&L (M VND)**")
    st.dataframe(df_pnl, hide_index=True)
    st.write("---")
    st.write("**Cash Flow (M VND)**")
    st.dataframe(df_cfo, hide_index=True)

# --- 4. DASHBOARD CHÍNH ---
st.header("BNM FINANCIAL COMMAND CENTER")
st.caption("Coffee Division Operations // Strategy Optimization")

m1, m2, m3 = st.columns(3)
m1.metric("Gross Profit Margin", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Avg")
m3.metric("Cash Runway", "5.1 Months", "🎯 Target")

st.write("---")

col_left, col_right = st.columns([1, 1.3]) # Ưu tiên không gian cho biểu đồ 3D

with col_left:
    # Revenue/Expenses Line Chart
    fig_line = go.Figure()
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Revenue'], name='Net Revenue', line=dict(color='#00CC96', width=3)))
    fig_line.add_trace(go.Scatter(x=df_pnl['Month'], y=df_pnl['Expenses'], name='Expenses', line=dict(color='#EF553B', width=3)))
    fig_line.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(l=0, r=0, t=20, b=0))
    st.plotly_chart(fig_line, use_container_width=True)

    # CFO Bar Chart
    fig_bar = px.bar(df_cfo, x='Category', y=['Depreciation', 'Net Income', 'Inventory'],
                     color_discrete_map={'Depreciation': '#00CC96', 'Net Income': '#EF553B', 'Inventory': '#FECB52'},
                     barmode='relative', template="plotly_dark")
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350, margin=dict(l=0, r=0, t=20, b=0))
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("[02] OPERATIONS_EFFICIENCY")
    # --- CHIÊU CUỐI: TẠO MESH GRID NHẤP NHÔ DÀY ĐẶC (GIỐNG ẢNH MẪU 100%) ---
    x = np.outer(np.linspace(-3, 3, 50), np.ones(50))
    y = x.copy().T
    # Hàm sóng kết hợp để tạo độ nhấp nhô dày đặc
    z = (np.sin(x**2 + y**2) * np.cos(x*y) * 0.5 + 
         0.2 * np.sin(10*x) * np.cos(10*y)) # Tạo thêm các "gai" nhỏ mượt mà
    
    # Dùng màu Viridis hoặc Greys tùy sở thích, nhưng Viridis nhìn chuyên nghiệp hơn
    fig_3d = go.Figure(data=[go.Surface(z=z, colorscale='Viridis', showscale=False)])
    
    fig_3d.update_layout(
        scene=dict(
            xaxis=dict(visible=False),
            yaxis=dict(visible=False),
            zaxis=dict(visible=False),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=0.5) # Làm bẹt biểu đồ xuống cho giống ảnh mẫu
        ),
        margin=dict(l=0, r=0, b=0, t=0), 
        height=750, 
        paper_bgcolor='rgba(0,0,0,0)'
    )
    st.plotly_chart(fig_3d, use_container_width=True)

st.info("💡 **OPTIMIZATION:** Điều chỉnh nhân sự ca 10 sáng để tối ưu hóa mật độ đỉnh (Peaks).")
