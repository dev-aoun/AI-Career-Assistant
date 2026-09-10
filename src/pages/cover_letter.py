import streamlit as st

from src.cover_letter.generator import generate_cover_letter


def cover_letter_page():

    st.title("✉️ AI Cover Letter Generator")

    st.write(
        "Generate a professional cover letter in seconds."
    )

    name = st.text_input(
        "👤 Full Name",
        placeholder="Muhammad Aoun"
    )

    position = st.text_input(
        "💼 Job Position",
        placeholder="Python Developer"
    )

    skills = st.text_area(
        "🛠 Skills",
        placeholder="Python, SQL, AI, Streamlit, Docker"
    )

    experience = st.text_area(
        "📄 Experience / Projects",
        placeholder="Describe your projects or experience..."
    )

    tone = st.selectbox(
        "🎨 Writing Tone",
        [
            "Professional",
            "Formal",
            "Friendly",
            "Confident",
        ],
    )

    if st.button("🚀 Generate Cover Letter", use_container_width=True):

        if not name or not position:
            st.warning("Please enter your name and job position.")
            return

        letter = generate_cover_letter(
            name=name,
            position=position,
            skills=skills,
            experience=experience,
            tone=tone,
        )

        st.success("✅ Cover Letter Generated")

        st.text_area(
            "Generated Cover Letter",
            letter,
            height=400,
        )

        st.download_button(
            "📥 Download Cover Letter",
            data=letter,
            file_name="cover_letter.txt",
            mime="text/plain",
            use_container_width=True,
        )