import streamlit as st

def init_state():
    if "page" not in st.session_state:
        st.session_state.page = "menu"

def go(page: str):
    st.session_state.page = page
    st.rerun()
