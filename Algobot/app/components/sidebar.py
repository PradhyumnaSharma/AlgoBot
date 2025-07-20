import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.title("Navigation")
        if st.button("Home"):
            st.session_state.page = "main"
        if st.button("History"):
            st.session_state.page = "history"
        if st.button("Previous Doubts"):
            st.session_state.page = "doubts"