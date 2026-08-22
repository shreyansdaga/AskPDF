import streamlit as st
import requests

st.title("AskPDF")

uploaded_file = st.file_uploader("Choose a pdf file", type=["pdf"])

if uploaded_file is not None:
    # Detect a new/different file and reset session state tied to the previous one
    if st.session_state.get("current_file") != uploaded_file.name:
        st.session_state.current_file = uploaded_file.name
        st.session_state.file_saved = False

    if not st.session_state.file_saved:
        response = requests.post(
            "http://localhost:8000/ingest",
            files={"file": (uploaded_file.name, uploaded_file.getbuffer(), "application/pdf")}
        )
        st.session_state.file_saved = True

    user_text = st.text_input("Enter your question here:")

    if st.button("Ask"):
        st.write("Your question was:", user_text)
        response = requests.post(
            "http://localhost:8000/ask_question",
            json={"question": user_text}
        )
        answer = response.json()
        st.write("Answer: ", answer["answer"])
