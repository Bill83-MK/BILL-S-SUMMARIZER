import streamlit as st

st.title("Bill's Summarizer")
st.write("This is a simple text summarizer app.")

# Add a text input area
user_input = st.text_area("Enter text to summarize:", "")

if st.button("Summarize"):
    if user_input:
        summary = user_input[:100] + "..."  # Replace with actual summarization logic
        st.write("### Summary:")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")
