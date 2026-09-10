import streamlit as st


def hero():

    st.markdown(
        """
        <div class="hero-box">

        <h1 class="hero-title">
        🚀 AI Career Assistant
        </h1>

        <p class="hero-subtitle">

        Build smarter resumes, improve ATS scores,
        match jobs, prepare interviews,
        and accelerate your career with AI.

        </p>

        </div>

        """,
        unsafe_allow_html=True
    )