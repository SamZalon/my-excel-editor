import streamlit as st

st.set_page_config(page_title="Excel Editor", layout="centered", initial_sidebar_state="collapsed")

st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap');

        .stApp {
            background-color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        header, footer, #MainMenu {visibility: hidden;}

        .main-title {
            font-size: 64px;
            font-weight: 600;
            color: #263238;
            text-align: center;
            margin-top: 15vh;
            margin-bottom: 50px;
            line-height: 76px;
        }

        div.stButton > button {
            background-color: #2BCB8B;
            color: #FFFFFF;
            border-radius: 4px;
            font-size: 16px;
            font-weight: 400;
            border: none;
            width: 100%;
            height: 48px;
            transition: 0.2s;
        }

        div.stButton > button:hover {
            background-color: #43A048;
            color: #FFFFFF;
        }

        .secondary-btn div.stButton > button {
            background-color: #FFFFFF;
            color: #263238;
            border: 1px solid #A8BED1;
        }

        .secondary-btn div.stButton > button:hover {
            background-color: #F5F7FA;
            color: #263238;
            border: 1px solid #89939E;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Excel Editor</div>', unsafe_allow_html=True)

_, col1, col2, _ = st.columns([1, 1.5, 1.5, 1])

with col1:
    st.button("Upload File")

with col2:
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    st.button("Upload Data by Link")
    st.markdown('</div>', unsafe_allow_html=True)
