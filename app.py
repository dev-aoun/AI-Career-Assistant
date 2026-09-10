import streamlit as st
from src.pages.resume_parser import resume_parser_page
from src.components.sidebar import sidebar
from src.components.header import header
from src.pages.skill_gap import skill_gap_page
from src.pages.job_matcher import job_matcher_page
from src.pages.ats_score import ats_score_page
from src.pages.interview import interview_page
from src.pages.cover_letter import cover_letter_page
from src.pages.chatbot import chatbot_page

# ==========================
# Page Configuration
# ==========================
st.set_page_config(
    page_title="AI Career Assistant",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ==========================
# Imports
# ==========================
from src.utils.theme import load_css
from src.components.hero import hero
from src.components.cards import feature_card
from src.components.metrics import metric_card
from src.components.footer import footer

# ==========================
# Load CSS
# ==========================
load_css()

# ==========================
# Sidebar
# ==========================
page = sidebar()

# ==========================================================
# HOME PAGE
# ==========================================================
if page == "🏠 Home":

    # Header
    header()

    st.write("")

    # Hero
    hero()

    st.write("")
    
    # Action Buttons
    col1, col2 = st.columns(2)

    with col1:
        st.button(
            "📄 Upload Resume",
            use_container_width=True,
        )

    with col2:
        st.button(
            "🚀 Explore Features",
            use_container_width=True,
        )

    st.divider()

    st.subheader("✨ AI Features")

    c1, c2, c3 = st.columns(3)

    with c1:
        feature_card(
            "📄",
            "Resume Parser",
            "Upload PDF or DOCX resumes and extract useful information."
        )

        feature_card(
            "🎯",
            "ATS Resume Score",
            "Analyze your resume and improve ATS compatibility."
        )

    with c2:
        feature_card(
            "💼",
            "Job Matcher",
            "Compare your resume with a Job Description."
        )

        feature_card(
            "📈",
            "Skill Gap Analyzer",
            "Discover missing skills and learning recommendations."
        )

    with c3:
        feature_card(
            "🎤",
            "Interview Questions",
            "Generate AI-powered interview questions."
        )

        feature_card(
            "🤖",
            "Career Chatbot",
            "Get AI career guidance and advice."
        )

    st.divider()

    st.subheader("📊 Dashboard")

    m1, m2, m3 = st.columns(3)

    with m1:
        metric_card("📄 Features", "7")

    with m2:
        metric_card("🤖 AI Accuracy", "95%")

    with m3:
        metric_card("🚀 Modules", "7")

    footer()

# ==========================================================
# RESUME PARSER
# ==========================================================
elif page == "📄 Resume Parser":
    resume_parser_page()
# ==========================================================
# ATS SCORE
# ==========================================================
elif page == "🎯 ATS Score":

    ats_score_page()
# ==========================================================
# JOB MATCHER
# ==========================================================
elif page == "💼 Job Matcher":

    job_matcher_page()
# ==========================================================
# SKILL GAP
# ==========================================================
elif page == "📈 Skill Gap":

    skill_gap_page()

# ==========================================================
# INTERVIEW
# ==========================================================
elif page == "🎤 Interview Questions":

    interview_page()

# ==========================================================
# COVER LETTER
# ==========================================================
elif page == "✉️ Cover Letter":

    cover_letter_page()

# ==========================================================
# CHATBOT
# ==========================================================
elif page == "🤖 Career Chatbot":

    chatbot_page()