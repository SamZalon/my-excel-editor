import streamlit as st
import pandas as pd
import io

# ตั้งค่าหน้าเว็บ
st.set_page_config(page_title="My Excel Editor", layout="wide")
st.title(" Personal Excel Editor")

# ส่วนที่ 1: การ Import ไฟล์
uploaded_file = st.file_uploader("เลือกไฟล์ Excel ของคุณเพื่อเริ่มต้น", type=['xlsx', 'xls'])

if uploaded_file is not None:
    # อ่านไฟล์ Excel
    df = pd.read_excel(uploaded_file)
    st.success("อัปโหลดไฟล์สำเร็จ!")

    # ส่วนที่ 2: การแสดงผลและแก้ไขข้อมูล
    st.subheader("แก้ไขข้อมูลของคุณ")
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    # ส่วนที่ 3: การ Export ออกไป
    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
        edited_df.to_excel(writer, index=False, sheet_name='Sheet1')

    st.markdown("---")
    # ปุ่มดาวน์โหลด
    st.download_button(
        label=" ดาวน์โหลดไฟล์ Excel ที่อัปเดตแล้ว",
        data=buffer.getvalue(),
        file_name="updated_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )
else:
    st.info(" กรุณาอัปโหลดไฟล์ Excel เพื่อเริ่มการทำงาน")