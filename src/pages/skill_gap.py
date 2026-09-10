import os
import streamlit as st

from src.resume_parser.parser import parse_resume_file
from src.skill_gap.roles import ROLE_SKILLS
from src.skill_gap.analyzer import analyze_skill_gap
from src.skill_gap.roadmap import generate_learning_roadmap


def skill_gap_page():

    st.title("📈 Skill Gap Analyzer")

    st.write(
        "Upload your resume and select a target role "
        "to identify missing skills."
    )

    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx"],
        key="skill_gap_resume"
    )

    target_role = st.selectbox(
        "🎯 Select Target Role",
        list(ROLE_SKILLS.keys())
    )

    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:

            resume = parse_resume_file(file_path)

            result = analyze_skill_gap(
                resume.skills,
                target_role
            )

            roadmap = generate_learning_roadmap(
                result["missing_skills"]
            )

            st.success("✅ Skill Gap Analysis Complete!")

            # ==========================
            # Completion
            # ==========================

            st.subheader("🎯 Skill Match")

            st.metric(
                "Skill Completion",
                f"{result['completion']}%"
            )

            st.progress(
                result["completion"] / 100
            )

            # ==========================
            # Current Skills
            # ==========================

            st.subheader("✅ Your Skills")

            if result["current_skills"]:
                st.write(
                    ", ".join(result["current_skills"])
                )
            else:
                st.info("No matching skills found.")

            # ==========================
            # Missing Skills
            # ==========================

            st.subheader("❌ Missing Skills")

            if result["missing_skills"]:
                st.write(
                    ", ".join(result["missing_skills"])
                )
            else:
                st.success(
                    "🎉 You have all the required skills!"
                )

            # ==========================
            # Learning Roadmap
            # ==========================

            st.subheader("🚀 Learning Roadmap")

            if roadmap:

                for item in roadmap:

                    priority = item["priority"]

                    st.markdown(
                        f"### {item['skill']} — {priority} Priority"
                    )

                    st.write(
                        item["recommendation"]
                    )

                    st.divider()

            else:

                st.success(
                    "No learning gaps identified."
                )

        except Exception as e:

            st.error(
                f"Error analyzing resume: {e}"
            )