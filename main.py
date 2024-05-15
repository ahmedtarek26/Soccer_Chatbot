import streamlit as st
from langchain_helper import get_db_chain

st.title("StatsBomb AFCON 2023, WC 2022, Women's WC 2022: Matches Database Q&A 👕")

question = st.text_input("Question: ")

if question:
    chain = get_db_chain()
    response = chain.run(question)

    st.header("Answer")
    st.write(response)