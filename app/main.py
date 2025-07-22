import streamlit as st
import templates_viewer, problem_browser

st.sidebar.title("🧠 LeetCode Practice UI")
page = st.sidebar.selectbox("Choose Page", ["Templates", "Problems"])

if page == "Templates":
    templates_viewer.show()
else:
    problem_browser.show()
