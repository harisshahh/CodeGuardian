import streamlit as st
import requests

st.title("Code Guardian")
code = st.text_area("Paste your code below")
goal = st.selectbox("What do you want to do?", ["Explain", "Debug", "Optimize"])

if st.button("Analyze")
    res = requests.post("http://localhost:8000/analyze", json = {"code": code, "goal": goal})
    st.subheader("AI Response")
    st.write(res.json()["result"])