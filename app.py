import streamlit as st

st.set_page_config(page_title="Excel Editor", layout="wide", initial_sidebar_state="expanded")

# Custom CSS according to Style Guide
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        /* Main App Style */
        .stApp {
            background-color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        header, footer, #MainMenu {visibility: hidden;}

        /* Centered Title at Top */
        .centered-title {
            font-size: 64px;
            font-weight: 600;
            color: #232321;
            text-align: center;
            width: 100%;
            margin-top: -50px;
            padding-bottom: 20px;
            border-bottom: 1px solid #F5F7FA;
        }

        /* Sidebar Style */
        section[data-testid="stSidebar"] {
            background-color: #FDFDFD;
            border-right: 1px solid #E8ECEF;
            width: 300px !important;
        }

        /* Sidebar Buttons */
        .stSidebar div.stButton > button {
            background-color: #38CB89;
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
            background-color: #2EB376;
        }

        /* Secondary Button in Sidebar */
        .secondary-sidebar div.stButton > button {
            background-color: #FFFFFF;
            color: #232321;
            border: 1px solid #A8BED1;
        }

        .secondary-sidebar div.stButton > button:hover {
            background-color: #F5F7FA;
            border: 1px solid #89939E;
        }
        
        /* Sidebar Title Header */
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

# Main Content
st.markdown('<div class="centered-title">Excel Editor</div>', unsafe_allow_html=True)

# Sidebar Content
with st.sidebar:
    st.markdown('<div class="sidebar-header">Tools</div>', unsafe_allow_html=True)
    
    st.button("Upload File")
    
    st.markdown('<div class="secondary-sidebar">', unsafe_allow_html=True)
    st.button("Upload Data by Link")
    st.markdown('</div>', unsafe_allow_html=True)


Your slide deck on Personal Excel Editor with the updated UI design is ready! I've placed the title centered at the top and moved the buttons into a styled left sidebar based on your style guide. Feel free to take a look and let me know if you'd like to adjust anything else.
