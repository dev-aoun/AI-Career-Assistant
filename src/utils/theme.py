import streamlit as st


def load_css():
    """Load custom CSS into the Streamlit app."""
    with open("assets/styles.css", encoding="utf-8") as css_file:
        st.markdown(
            f"<style>{css_file.read()}</style>",
            unsafe_allow_html=True,
        )