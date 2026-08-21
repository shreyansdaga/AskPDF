import streamlit as st
import os

st.title("AskPDF")

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

uploaded_file = st.file_uploader("Choose a pdf file", type=["pdf"])

if uploaded_file is not None:
    # Detect a new/different file and reset session state tied to the previous one
    if st.session_state.get("current_file") != uploaded_file.name:
        st.session_state.current_file = uploaded_file.name
        st.session_state.file_saved = False

    file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

    if not st.session_state.file_saved:
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.session_state.file_saved = True

    user_text = st.text_input("Enter your question here:")
    st.write("Your question was:", user_text)
