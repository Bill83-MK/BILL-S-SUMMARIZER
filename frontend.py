import streamlit as st
import requests

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/summarize"

st.set_page_config(page_title="AI News Summarizer", layout="wide")

st.markdown("## 📢BILL'S SUMMARIZER")
st.write("Fetching latest news...")

# Text input for news content
text_input = st.text_area("Enter news text to summarize", height=200)

if st.button("Summarize"):
    if text_input.strip():
        response = requests.post(API_URL, json={"text": text_input})
        if response.status_code == 200:
            summary = response.json()["summary"]
            st.markdown(f"### Summary: {summary}")
        else:
            st.error("Failed to summarize. Try again.")
    else:
        st.warning("Please enter text to summarize.")
