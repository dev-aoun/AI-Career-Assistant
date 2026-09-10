import streamlit as st

from src.chatbot.chatbot import chatbot_response


def chatbot_page():

    st.title("🤖 AI Career Chatbot")

    st.write(
        "Ask me anything about resumes, ATS, interviews, jobs, skills, or your career."
    )

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [
            (
                "assistant",
                "👋 Hello! I'm your AI Career Assistant. How can I help you today?"
            )
        ]

    # Display previous messages
    for role, message in st.session_state.messages:
        with st.chat_message(role):
            st.write(message)

    # Chat input
    prompt = st.chat_input("Type your question here...")

    if prompt:

        # Show user message
        st.session_state.messages.append(("user", prompt))

        with st.chat_message("user"):
            st.write(prompt)

        # Generate response
        response = chatbot_response(prompt)

        # Show assistant response
        st.session_state.messages.append(("assistant", response))

        with st.chat_message("assistant"):
            st.write(response)