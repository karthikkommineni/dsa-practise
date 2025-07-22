import streamlit as st
import os

TEMPLATE_DIR = "templates"

def show():
    st.title("📚 Coding Templates")
    templates = [f for f in os.listdir(TEMPLATE_DIR) if f.endswith(".py")]
    selected = st.selectbox("Select a Template", templates)

    if selected:
        with open(os.path.join(TEMPLATE_DIR, selected), "r") as f:
            code = f.read()
        st.code(code, language='python')
