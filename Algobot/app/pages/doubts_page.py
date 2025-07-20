import streamlit as st
from app.db.queries import fetch_all_doubts, delete_all_doubts

def render_doubts_page():
    st.title("Doubt History")
    if st.button("Delete All Doubts"):
        delete_all_doubts()
        st.success("All doubts history deleted.")

    rows = fetch_all_doubts()
    for row in rows:
        with st.expander(f"{row[1]}"):
            st.markdown(f"**Answer:**\n{row[2]}")
