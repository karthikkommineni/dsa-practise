import streamlit as st
import os

SOLUTION_DIR = "solutions"

def show():
    st.title("🧩 Problem Browser")
    topics = [d for d in os.listdir(SOLUTION_DIR) if os.path.isdir(os.path.join(SOLUTION_DIR, d))]
    selected_topic = st.selectbox("Topic", topics)

    if selected_topic:
        files = os.listdir(os.path.join(SOLUTION_DIR, selected_topic))
        problem = st.selectbox("Problem File", files)
        if problem:
            with open(os.path.join(SOLUTION_DIR, selected_topic, problem), "r") as f:
                code = f.read()
            st.code(code, language='python')
