import os
import streamlit as st

from src.resume_parser.parser import parse_resume_file
from src.job_matcher.matcher import calculate_job_match


def job_matcher_page():

    st.title("💼 Job Matcher")

    st.write(
        "Upload your resume and paste a Job Description "
        "to analyze your compatibility."
    )

    uploaded_file = st.file_uploader(
        "📄 Upload Resume",
        type=["pdf", "docx"],
        key="job_match_resume"
    )

    job_description = st.text_area(
        "📋 Paste Job Description",
        height=250,
        placeholder="Paste the complete job description here..."
    )

    if uploaded_file is not None and job_description.strip():

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:

            resume = parse_resume_file(file_path)

            result = calculate_job_match(
                resume,
                job_description
            )

            st.success("✅ Analysis Complete!")

            # ==========================
            # Match Score
            # ==========================

            st.subheader("🎯 Job Match Score")

            score = result["match_score"]

            st.metric(
                "Match Score",
                f"{score}%"
            )

            st.progress(score / 100)

            # ==========================
            # Required Skills
            # ==========================

            st.subheader("📋 Required Skills")

            if result["required_skills"]:
                st.write(", ".join(result["required_skills"]))
            else:
                st.info(
                    "No recognized technical skills "
                    "were found in the Job Description."
                )

            # ==========================
            # Matching Skills
            # ==========================

            st.subheader("✅ Matching Skills")

            if result["matched_skills"]:
                st.write(", ".join(result["matched_skills"]))
            else:
                st.info("No matching skills found.")

            # ==========================
            # Missing Skills
            # ==========================

            st.subheader("❌ Missing Skills")

            if result["missing_skills"]:
                st.write(", ".join(result["missing_skills"]))
            else:
                st.success("No missing skills!")

            # ==========================
            # Feedback
            # ==========================

            feedback = result["feedback"]

            st.subheader("📝 Overall Feedback")

            st.info(feedback["overall"])

            st.subheader("🚀 Suggestions")

            if feedback["suggestions"]:

                for suggestion in feedback["suggestions"]:
                    st.write("•", suggestion)

            else:
                st.success(
                    "Your resume is well aligned with this job."
                )

        except Exception as e:

            st.error(f"Error analyzing resume: {e}")

    elif uploaded_file is not None:

        st.info(
            "Please paste a Job Description to continue."
        )