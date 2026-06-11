import streamlit as st

st.set_page_config(page_title="Excel Editor", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS based on the provided Style Guide
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

        /* Typography & Colors */
        .stApp {
            background-color: #FFFFFF;
            font-family: 'Inter', sans-serif;
        }

        header, footer, #MainMenu {visibility: hidden;}

        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 120px;
            text-align: center;
        }

        /* Headline 1 */
        .headline-1 {
            font-size: 64px;
            font-weight: 600;
            color: #232321;
            margin-bottom: 16px;
            line-height: 76px;
        }

        /* Body 1 */
        .body-1 {
            font-size: 18px;
            color: #646464;
            margin-bottom: 48px;
            line-height: 28px;
        }

        /* Primary Button Style */
        div.stButton > button {
            background-color: #38CB89;
            color: #FFFFFF;
            border-radius: 8px;
            padding: 12px 32px;
            font-size: 16px;
            font-weight: 500;
            border: none;
            width: 240px;
            height: 56px;
            transition: all 0.2s ease;
            box-shadow: 0px 4px 12px rgba(56, 203, 137, 0.2);
        }

        div.stButton > button:hover {
            background-color: #2EB376;
            color: #FFFFFF;
            box-shadow: 0px 6px 16px rgba(56, 203, 137, 0.3);
        }

        /* Secondary Button Style */
        .secondary-btn div.stButton > button {
            background-color: #E8F9F1;
            color: #38CB89;
            box-shadow: none;
        }

        .secondary-btn div.stButton > button:hover {
            background-color: #D1F2E2;
            color: #2EB376;
            box-shadow: none;
        }

        [data-testid="column"] {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)

# Layout
st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="headline-1">Excel Editor</h1>', unsafe_allow_html=True)
st.markdown('<p class="body-1">Professional tool to import, edit, and fill missing data effectively.</p>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.button("Upload File")

with col2:
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    st.button("Upload Data by Link")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
