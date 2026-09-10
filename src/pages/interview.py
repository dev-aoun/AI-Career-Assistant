import streamlit as st

from src.interview.generator import generate_questions


def interview_page():

    st.title("🎤 Interview Question Generator")

    st.write(
        "Generate interview questions based on your selected role."
    )

    # Job Role
    role = st.selectbox(
        "💼 Select Job Role",
        [
            "Software Engineer",
            "Python Developer",
            "AI Engineer",
            "Data Analyst",
        ],
    )

    # Interview Type
    interview_type = st.radio(
        "📋 Interview Type",
        [
            "HR",
            "Technical",
            "Mixed",
        ],
        horizontal=True,
    )

    # Difficulty
    difficulty = st.selectbox(
        "📊 Difficulty",
        [
            "Easy",
            "Medium",
            "Hard",
        ],
    )

    # Generate Button
    if st.button("🚀 Generate Questions", use_container_width=True):

        questions = generate_questions(role, interview_type)

        st.success(
            f"Generated {len(questions)} {difficulty} interview questions."
        )

        st.divider()

        for i, question in enumerate(questions, start=1):

            st.markdown(
                f"""
                <div class="card">
                    <h3>Question {i}</h3>
                    <p>{question}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )