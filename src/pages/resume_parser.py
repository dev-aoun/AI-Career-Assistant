import os
import importlib

st = importlib.import_module("streamlit")

from src.resume_parser.parser import parse_resume_file
from src.ai.resume_analyzer import analyze_resume_with_ai


def resume_parser_page():

    st.title("📄 Resume Parser")

    st.write(
        "Upload your resume (PDF or DOCX) to extract structured information."
    )

    uploaded_file = st.file_uploader(
        "Choose Resume",
        type=["pdf", "docx"]
    )

    if uploaded_file is None:
        return

    os.makedirs("uploads", exist_ok=True)

    save_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    try:

        # ======================================
        # Parse Resume
        # ======================================

        resume = parse_resume_file(save_path)

        st.success("✅ Resume Parsed Successfully!")

        # ======================================
        # Personal Information
        # ======================================

        st.header("👤 Personal Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Name:**", resume.name)
            st.write("**Email:**", resume.email)
            st.write("**Phone:**", resume.phone)

        with col2:
            st.write("**LinkedIn:**", resume.linkedin)
            st.write("**GitHub:**", resume.github)

        # ======================================
        # Skills
        # ======================================

        st.header("🛠 Skills")

        if resume.skills:
            st.write(", ".join(resume.skills))
        else:
            st.info("No skills found.")

        # ======================================
        # Education
        # ======================================

        st.header("🎓 Education")

        if resume.education:

            for edu in resume.education:

                st.markdown(
                    f"### {edu.get('degree', '')}"
                )

                if edu.get("institution"):
                    st.write(
                        "🏫",
                        edu["institution"]
                    )

                if edu.get("duration"):
                    st.write(
                        "📅",
                        edu["duration"]
                    )

                st.divider()

        else:
            st.info("No education found.")

        # ======================================
        # Experience
        # ======================================

        st.header("💼 Experience")

        if resume.experience:

            for exp in resume.experience:

                st.markdown(
                    f"### {exp.get('title', '')}"
                )

                if exp.get("company"):
                    st.write(
                        "🏢",
                        exp["company"]
                    )

                if exp.get("duration"):
                    st.write(
                        "📅",
                        exp["duration"]
                    )

                if exp.get("description"):

                    for item in exp["description"]:

                        clean_item = item.lstrip("-• ").strip()

                        if clean_item:
                            st.write(
                                "•",
                                clean_item
                            )

                st.divider()

        else:
            st.info("No experience found.")

        # ======================================
        # Projects
        # ======================================

        st.header("🚀 Projects")

        if resume.projects:

            for project in resume.projects:

                st.markdown(
                    f"### {project.get('title', '')}"
                )

                if project.get("description"):

                    for item in project["description"]:

                        clean_item = item.lstrip("-• ").strip()

                        if clean_item:
                            st.write(
                                "•",
                                clean_item
                            )

                st.divider()

        else:
            st.info("No projects found.")

        # ======================================
        # Certifications
        # ======================================

        st.header("📜 Certifications")

        if resume.certifications:

            for cert in resume.certifications:

                clean_cert = cert.lstrip("-• ").strip()

                if clean_cert:
                    st.write(
                        "•",
                        clean_cert
                    )

        else:
            st.info("No certifications found.")

        # ======================================
        # Languages
        # ======================================

        st.header("🌍 Languages")

        if resume.languages:
            st.write(
                ", ".join(resume.languages)
            )
        else:
            st.info("No languages found.")

        # ======================================
        # AI Resume Analysis
        # ======================================

        st.divider()

        st.header("🤖 AI Resume Analysis")

        if st.button(
            "🚀 Analyze Resume with AI",
            use_container_width=True
        ):

            try:

                with st.spinner(
                    "AI is analyzing your resume..."
                ):

                    ai_analysis = analyze_resume_with_ai(
                        resume
                    )

                st.success(
                    "✅ AI Analysis Complete!"
                )

                st.markdown(ai_analysis)

            except Exception as e:

                st.error(
                    f"AI analysis failed: {e}"
                )

    except Exception as e:

        st.error(
            f"Error parsing resume: {e}"
        )