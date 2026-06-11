import streamlit as st

st.set_page_config(page_title="Excel Editor", layout="wide", initial_sidebar_state="expanded")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        .stApp {
            background-color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        header, footer, #MainMenu {visibility: hidden;}

        /* ซ่อนเฉพาะปุ่มพับเก็บด้านใน (กากบาท/ลูกศร) เพื่อให้ Sidebar ค้างไว้เสมอ */
        [data-testid="stSidebarCollapseButton"] {
            display: none !important;
        }

        .centered-title {
            font-size: 64px;
            font-weight: 600;
            color: #263238;
            text-align: center;
            width: 100%;
            margin-top: -50px;
            padding-bottom: 20px;
            border-bottom: 1px solid #F5F7FA;
        }

        section[data-testid="stSidebar"] {
            background-color: #FDFDFD;
            border-right: 1px solid #E8ECEF;
        }

        .stSidebar div.stButton > button {
            background-color: #2BCB8B;
            color: #FFFFFF;
            border-radius: 4px;
            font-size: 14px;
            font-weight: 500;
            border: none;
            width: 100%;
            height: 44px;
            margin-bottom: 10px;
            transition: 0.2s;
        }

        .stSidebar div.stButton > button:hover {
            background-color: #43A048;
        }

        .secondary-sidebar div.stButton > button {
            background-color: #FFFFFF;
            color: #263238;
            border: 1px solid #A8BED1;
        }

        .secondary-sidebar div.stButton > button:hover {
            background-color: #F5F7FA;
            border: 1px solid #89939E;
        }
        
        .sidebar-header {
            font-size: 14px;
            font-weight: 600;
            color: #89939E;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered-title">Excel Editor</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown('<div class="sidebar-header">Tools</div>', unsafe_allow_html=True)
    
    st.button("Upload File")
    
    st.markdown('<div class="secondary-sidebar">', unsafe_allow_html=True)
    st.button("Upload Data by Link")
    st.markdown('</div>', unsafe_allow_html=True)
