import streamlit as st


def show() -> None:
    """Render the AI Career Assistant home page."""
    st.title("💼 AI Career Assistant")

    st.markdown(
        """
        Welcome to the **AI Career Assistant**.

        This application helps users improve their employability using AI.
        """
    )

    st.subheader("Features")

    features = [
        "📄 Resume Parser",
        "🎯 ATS Resume Scoring",
        "💼 Job Description Matching",
        "📈 Skill Gap Analysis",
        "🎤 Interview Question Generator",
        "✉️ Cover Letter Generator",
        "🤖 AI Career Chatbot",
    ]

    st.markdown("\n".join(f"- {feature}" for feature in features))
    st.success("Select a feature from the sidebar.")