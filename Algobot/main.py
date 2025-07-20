from app import llm
from app.db.setup import init_db
from app.components.sidebar import render_sidebar
from app.pages.main_page import render_main_page
from app.pages.history_page import render_history_page
from app.pages.doubts_page import render_doubts_page

import streamlit as st

st.set_page_config("AlgoBot", layout="wide")
init_db()
render_sidebar()

if "page" not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    render_main_page()
elif st.session_state.page == "history":
    render_history_page()
elif st.session_state.page == "doubts":
    render_doubts_page()