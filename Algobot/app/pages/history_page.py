import streamlit as st
from app.db.queries import fetch_all_history, delete_all_history

def render_history_page():
    st.title("Previous Conversations")
    if st.button("Delete All History"):
        delete_all_history()
        st.success("All conversation history deleted.")

    rows = fetch_all_history()
    for row in rows:
        with st.expander(f"{row[1]}"):
            st.markdown(f"**Explanation:**\n{row[2]}")
            st.markdown(f"**Algorithm:**\n{row[3]}")
            st.markdown(f"**Quote:** _{row[4]}_")