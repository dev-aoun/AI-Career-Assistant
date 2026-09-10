import streamlit as st


def sidebar():
    st.sidebar.markdown(
        """
        <h2 style='text-align:center; color:white;'>
            🚀 AI Career Assistant
        </h2>
        """,
        unsafe_allow_html=True,
    )

    st.sidebar.markdown("---")

    page = st.sidebar.radio(
        "📂 Navigation",
        [
            "🏠 Home",
            "📄 Resume Parser",
            "🎯 ATS Score",
            "💼 Job Matcher",
            "📈 Skill Gap",
            "🎤 Interview Questions",
            "✉️ Cover Letter",
            "🤖 Career Chatbot",
        ],
    )

    st.sidebar.markdown("---")

    st.sidebar.markdown(
        """
        <div style="
        background:#2563EB;
        padding:15px;
        border-radius:12px;
        text-align:center;
        color:white;
        font-weight:bold;
        ">
        🚀 Version 1.0
        </div>
        """,
        unsafe_allow_html=True,
    )

    return page