import os
import streamlit as st

from src.resume_parser.parser import parse_resume_file
from src.ats_scorer.scorer import calculate_ats_score


def ats_score_page():

    st.title("🎯 ATS Resume Scorer")

    st.write(
        "Upload your resume and receive an ATS compatibility score."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"],
    )

    if uploaded_file is not None:

        os.makedirs("uploads", exist_ok=True)

        file_path = os.path.join(
            "uploads",
            uploaded_file.name,
        )

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        try:

            resume = parse_resume_file(file_path)

            result = calculate_ats_score(resume)

            score = result["score"]

            # ==========================
            # Score
            # ==========================

            st.success(f"ATS Score: {score}/100")

            st.progress(score / 100)

            # ==========================
            # Section Scores
            # ==========================

            st.subheader("📊 Section Scores")

            for section, value in result["section_scores"].items():
                st.write(f"**{section.title()}** : {value}")

            # ==========================
            # Matched Keywords
            # ==========================

            st.subheader("✅ Matched Keywords")

            if result["matched_keywords"]:
                st.write(", ".join(result["matched_keywords"]))
            else:
                st.info("No matched keywords found.")

            # ==========================
            # Missing Keywords
            # ==========================

            st.subheader("❌ Missing Keywords")

            if result["missing_keywords"]:
                st.write(", ".join(result["missing_keywords"][:20]))

            # ==========================
            # Feedback
            # ==========================

            feedback = result["feedback"]

            st.subheader("💪 Strengths")

            for item in feedback["strengths"]:
                st.success(item)

            st.subheader("⚠ Weaknesses")

            for item in feedback["weaknesses"]:
                st.warning(item)

            st.subheader("🚀 Suggestions")

            for item in feedback["suggestions"]:
                st.info(item)

        except Exception as e:

            st.error(str(e))