import streamlit as st

st.title("AskPDF")

uploaded_file = st.file_uploader("Choose a pdf file", type=["pdf"])

if uploaded_file is not None:
    name = uploaded_file.name

    with open(name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    user_text = st.text_input("Enter your question here:")
    st.write("Your question was:", user_text)