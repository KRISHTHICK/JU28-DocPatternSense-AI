import streamlit as st
from pattern_extractor import auto_detect_patterns
from pattern_approver import review_patterns
from doc_parser import parse_using_approved

st.title("📄 DocPatternSense – AI Pattern Extractor")

menu = ["1️⃣ Auto Pattern Detect", "2️⃣ Human Approve", "3️⃣ Apply Pattern"]
choice = st.sidebar.radio("Choose Step", menu)

if choice == menu[0]:
    uploaded_file = st.file_uploader("Upload DOCX", type="docx")
    if uploaded_file:
        with open("samples/complex_sample.docx", "wb") as f:
            f.write(uploaded_file.read())
        st.json(auto_detect_patterns("samples/complex_sample.docx"))

elif choice == menu[1]:
    review_patterns()

elif choice == menu[2]:
    st.write(parse_using_approved("samples/complex_sample.docx"))
