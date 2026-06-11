import streamlit as st

# --- 1. SET PAGE CONFIG ---
st.set_page_config(page_title="Excel Editor", layout="wide", initial_sidebar_state="collapsed")

# --- 2. CUSTOM CSS (Figma Minimal Style) ---
st.markdown("""
    <style>
        /* นำเข้าฟอนต์ Google Fonts - Kanit (คล้ายแบบ Figma) */
        @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;500;700&display=swap');

        /* พื้นหลังเว็บทั้งหมด */
        .stApp {
            background-color: #FDFDFD;
            font-family: 'Kanit', sans-serif;
        }

        /* ซ่อน Header และ Footer ของ Streamlit */
        header, footer, #MainMenu {visibility: hidden;}

        /* จัดวางตำแหน่งเนื้อหาให้อยู่กลางจอ */
        .main-container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            padding-top: 150px;
            text-align: center;
        }

        /* ตกแต่งชื่อหัวข้อ Excel Editor */
        .main-title {
            font-size: 85px !important;
            font-weight: 700 !important;
            color: #1A1A1A;
            margin-bottom: 10px;
            letter-spacing: -2px;
        }

        /* ตกแต่งคำอธิบายเล็กๆ */
        .sub-title {
            font-size: 20px;
            color: #666;
            margin-bottom: 50px;
            font-weight: 300;
        }

        /* ปรับแต่งปุ่ม Streamlit ให้ดู Minimal */
        div.stButton > button {
            background-color: #1A1A1A; /* สีดำ */
            color: white;
            border-radius: 50px; /* ขอบมนมากแบบ Figma */
            padding: 15px 45px;
            font-size: 18px;
            font-weight: 500;
            border: none;
            transition: all 0.3s ease;
            width: 280px;
            height: 65px;
            cursor: pointer;
        }

        /* เอฟเฟกต์ตอนเอาเมาส์ไปวางบนปุ่ม */
        div.stButton > button:hover {
            background-color: #444;
            color: white;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* ปรับแต่งปุ่มที่สอง (Secondary Style) */
        .secondary-btn div.stButton > button {
            background-color: transparent;
            color: #1A1A1A;
            border: 2px solid #1A1A1A;
        }
        
        .secondary-btn div.stButton > button:hover {
            background-color: #1A1A1A;
            color: white;
        }

        /* จัดการระยะห่างระหว่างปุ่ม */
        [data-testid="column"] {
            display: flex;
            justify-content: center;
        }
    </style>
""", unsafe_allow_html=True)




st.markdown('<div class="main-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-title">Excel Editor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Modern tool for cleaning and filling your missing data.</p>', unsafe_allow_html=True)


col1, col2 = st.columns(2)

with col1:
    
    st.button(" Upload File")

with col2:
    
    st.markdown('<div class="secondary-btn">', unsafe_allow_html=True)
    st.button(" Upload Data by Link")
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

