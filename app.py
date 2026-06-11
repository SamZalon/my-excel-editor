import streamlit as st

st.set_page_config(page_title="Excel Editor", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        .stApp {
            background-color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        header, footer, #MainMenu {visibility: hidden;}

        .centered-title {
            font-size: 64px;
            font-weight: 600;
            color: #263238;
            text-align: center;
            margin-top: 5vh;
            margin-bottom: 30px; 
        }

        div.stPopover > button {
            background-color: #2BCB8B;
            color: #Green;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 500;
            border: none;
            width: 200px;
            height: 48px;
            transition: 0.2s;
        }

        div.stPopover > button:hover {
            background-color: #43A048;
            color: #FFFFFF;
        }

        .popup-container div.stButton > button {
            background-color: #FFFFFF;
            color: #263238;
            border: 1px solid #A8BED1;
            border-radius: 4px;
            width: 160px;
            height: 40px;
            margin: 5px 0;
            font-size: 14px;
        }

        .popup-container div.stButton > button:hover {
            background-color: #F5F7FA;
            border: 1px solid #89939E;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="centered-title">Excel Editor</div>', unsafe_allow_html=True)

with st.popover("Upload"):
    st.markdown('<div class="popup-container">', unsafe_allow_html=True)
    st.button("Upload File", key="up_file")
    st.button("Upload Link", key="up_link")
    st.markdown('</div>', unsafe_allow_html=True)
