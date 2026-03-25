import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# --- 1. SETUP GIAO DIỆN ---
st.set_page_config(page_title="BNM Finance Lab", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    [data-testid="stSidebar"] { background-color: #161b22; border-right: 1px solid #30363d; }
    .stMetric { background-color: #1c2128; padding: 15px; border-radius: 8px; border: 1px solid #30363d; }
    div.block-container { padding-top: 1.5rem; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. DATA INPUT ---
pnl_data = {'Month': ['Jan', 'Feb', 'Mar'], 'Revenue': [5.896, 4.758, 6.241], 'Expenses': [10.044, 9.127, 8.655]}
df_pnl = pd.DataFrame(pnl_data)

cfo_data = {'Category': ['Actual', 'Target'], 'Depreciation': [41.7, 50.0], 'Net Income': [-54.1, -20.0], 'Inventory': [-6.8, -4.0]}
df_cfo = pd.DataFrame(cfo_data)

# --- 3. SIDEBAR ---
with st.sidebar:
    st.title("📂 BNM DATA")
    st.dataframe(df_pnl, hide_index=True)
    st.write("---")
    st.dataframe(df_cfo, hide_index=True)

# --- 4. GIAO DIỆN CHÍNH ---
st.header("FINANCIAL COMMAND CENTER")
st.caption("Coffee Division // PEAK_HOUR_DENSITY_3D Optimization")

m1, m2, m3 = st.columns(3)
m1.metric("Gross Margin", "41.4%", "↑ 2.1%")
m2.metric("Burn Rate (Avg)", "6.8M VND", "Normal")
m3.metric("Cash Runway", "5.1 Months", "🎯 Target")

st.write("---")

col_left, col_right = st.columns([1, 1.2])

with col_left:
    # Biểu đồ đường
    fig_line = px.line(df_pnl, x='Month', y=['Revenue', 'Expenses'], markers=True, template="plotly_dark")
    fig_line.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=350)
    st.plotly_chart(fig_line, use_container_width=True)

    # Biểu đồ cột
    fig_bar = px.bar(df_cfo, x='Category', y=['Depreciation', 'Net Income', 'Inventory'], barmode='relative', template="plotly_dark")
    fig_bar.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0_0,0)', height=350)
    st.plotly_chart(fig_bar, use_container_width=True)

with col_right:
    st.subheader("[02] OPERATIONS_EFFICIENCY")
    # --- ĐÃ FIX: TẠO NHIỀU NGỌN NÚI NHẤP NHÔ (MULTI-PEAK) ---
    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    X, Y = np.meshgrid(x, y)
    
    # Hàm tạo nhiều đỉnh núi đan xen
    Z = (np.cos(X)*np.sin(Y) + np.exp(-(X**2 + Y**2)/4) + 
         0.5*np.exp(-((X-2)**2 + (Y-2)**2)) + 
         0.5*np.exp(-((X+2)**2 + (Y+2)**2)))
    
    # Sử dụng màu 'Viridis' hoặc 'Turbo' để ra dải màu mượt mà như sếp muốn
    fig_3d = go.Figure(data=[go.Surface(z=Z, colorscale='Viridis', showscale=False)])
    
    fig_3d.update_layout(scene=dict(xaxis_visible=False, yaxis_visible=False, zaxis_visible=False), 
                        margin=dict(l=0, r=0, b=0, t=0), height=700, paper_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig_3d, use_container_width=True)

st.info("💡 **OPTIMIZATION:** Tăng staff ca sáng để tối ưu hóa các đỉnh (Peaks) vận hành.")
