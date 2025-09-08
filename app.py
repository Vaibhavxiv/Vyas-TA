import streamlit as st
from response import answer_query

st.set_page_config(page_title="Vyas Teaching Assistant", layout="centered")
st.title(" 📚 Vyas Teaching Assistant ")
query=st.text_input("💬 Enter your query here:",placeholder="Type your query related to course here.....")

if st.button("Ask"):
    if query:
        with st.spinner("Generating response..."):
            response,chunks = answer_query(query)
        st.subheader("🤖 Assistant's Answer")
        st.write(response)
        with st.expander("🔎 Relevant Chunks Used"):
            st.json(chunks[["title", "number", "start", "end", "text"]].to_dict(orient="records"))
    else:
        st.warning("Please enter a query.")
