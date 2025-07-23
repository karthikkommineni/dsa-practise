import streamlit as st
import templates_viewer, problem_browser
from app import python_notes

st.sidebar.title("🧠 LeetCode Practice UI")
page = st.sidebar.selectbox("Choose Page", ["Templates", "Problems", "Python Notes"])

if page == "Templates":
    templates_viewer.show()
elif page == "Problems":
    problem_browser.show()
else:
    python_notes.show_python_notes()

