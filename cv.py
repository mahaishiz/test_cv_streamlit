from pathlib import Path
import streamlit as st
from PIL import Image
import webbrowser

# Paths to assets
current_dir = Path(__file__).parent
css_file = current_dir / "styles/main.css"
cv_file = current_dir / "assets/Ziyad Mahaishiz_CV-2.pdf"
photo_p = current_dir / "assets/pp.jpeg"

# General settings
page_title = "Ziyad Mahaishiz"
location = "Malang, Jawa Timur"
page_icon = ":wave:"
name = "Ziyad Mahaishiz"
description = """
Ziyad Mahaishiz is a third-year law student at Brawijaya University 
with an interest in cyber law and legal tech. To enhance his knowledge 
in these fields, he pursues studies in Data Science and Artificial Intelligence (AI).
"""
email = "ziyadmahaishiz@student.ub.ac.id"
linked_in = "https://www.linkedin.com/in/ziyad-mahaishiz-26659b265/"

# Page configuration
st.set_page_config(page_title=page_title, page_icon=page_icon)

# Load CSS
with open(css_file) as css:
    st.markdown(f"<style>{css.read()}</style>", unsafe_allow_html=True)

# Load assets
with open(cv_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

photo_p = Image.open(photo_p)

# Page layout
st.title(page_title)

# Header section
col1, col2 = st.columns(2, gap="small")
with col1:
    st.write(description)

with col2:
    st.write("**Contact:**")
    st.write(email)
    if st.button("LinkedIn"):
        webbrowser.open(linked_in)

# Photo section
col3, col4 = st.columns(2, gap="small")
with col4:
    st.image(photo_p, width=150)

# Education section
st.subheader("Education")
col5, col6 = st.columns(2, gap="large")
with col5:
    st.write("**Universitas Brawijaya**")

with col6:
    st.write("**2022-2026**")

# Experience section
st.subheader("Experience")
st.write("- **Librarian & Database Administrator**, Muhammadiyah Plus Batam School")
st.write("- **Intern**, Badan Eksekutif Mahasiswa FH UB (Budpora)")
st.write("- **Event Division**, FH UB Class of 2022 Inauguration Night")

# Certification section
st.subheader("Certification")
st.write("- **CS50’s Introduction to Programming with Python**, Harvard University CS50")
st.write("- **CS50’s Introduction to Databases with SQL**, Harvard University CS50")

# Technical Skills section
st.subheader("Technical Skills")
st.write("""
- Database
- Spreadsheet
- SQL / SQLite
- Python
- Google Workspace (Gmail, Drive, Docs, Sheets, Slides, Forms)
- MS Office (Word, PowerPoint, Excel)
""")
