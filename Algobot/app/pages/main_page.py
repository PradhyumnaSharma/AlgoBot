import streamlit as st
from app.components.reasoning_agent import ReasoningAgent
from app.components.coding_agent import CodingAgent
from app.db.queries import save_history, save_doubt
from app import llm
from langchain_core.messages import HumanMessage

def render_main_page():
    st.title("AlgoBot - The Coding Wizard")
    st.markdown("_Your AI-Powered Coding Wizard_")
    st.markdown("_Code smarter. Learn faster. Dominate every problem._")

    if "reasoning" not in st.session_state:
        st.session_state.reasoning = None
    if "coding" not in st.session_state:
        st.session_state.coding = None

    input_type = st.radio("Choose input method", ["Paste Problem Link", "Paste Full Question"])
    question = ""
    if input_type == "Paste Problem Link":
        link = st.text_input("Enter Problem link")
        if link:
            question = f"Solve the problem at this link: {link}"
    else:
        question = st.text_area("Paste the full LeetCode-style problem", height=300)

    if st.button("Generate Solutions") and question:
        with st.spinner("Running Reasoning Agent..."):
            st.session_state.reasoning = ReasoningAgent(question)

        with st.spinner("Running Coding Agent..."):
            st.session_state.coding = CodingAgent(question)

        save_history(question, st.session_state.reasoning["explanation"],
                     st.session_state.reasoning["algorithm"], st.session_state.reasoning["quote"])

    if st.session_state.reasoning and st.session_state.coding:
        st.subheader("Explanation")
        st.markdown(st.session_state.reasoning["explanation"] or "(No explanation provided.)")

        st.subheader("Algorithm")
        st.markdown(st.session_state.reasoning["algorithm"] or "(No algorithm provided.)")

        tabs = st.tabs(["Python", "C++", "Java"])
        with tabs[0]:
            st.markdown("#### Brute Force")
            st.code(st.session_state.coding["py_brute"], language="python")
            st.markdown("#### Optimal")
            st.code(st.session_state.coding["py_opt"], language="python")
        with tabs[1]:
            st.markdown("#### Brute Force")
            st.code(st.session_state.coding["cpp_brute"], language="cpp")
            st.markdown("#### Optimal")
            st.code(st.session_state.coding["cpp_opt"], language="cpp")
        with tabs[2]:
            st.markdown("#### Brute Force")
            st.code(st.session_state.coding["java_brute"], language="java")
            st.markdown("#### Optimal")
            st.code(st.session_state.coding["java_opt"], language="java")

        st.subheader("Today's Quote")
        st.success(st.session_state.reasoning["quote"] or "Keep pushing. You're learning something great!")

        st.divider()
        st.subheader("Doubt?")
        doubt = st.text_area("Type your doubt here")
        if st.button("Solve Doubt") and doubt:
            with st.spinner("Answering your doubt..."):
                response = llm.invoke([HumanMessage(content=doubt)]).content
                st.markdown(response)
                save_doubt(doubt, response)
