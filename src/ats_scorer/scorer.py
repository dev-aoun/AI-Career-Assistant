from src.ats_scorer.rules import SECTION_WEIGHTS
from src.ats_scorer.keywords import ALL_KEYWORDS
from src.ats_scorer.feedback import generate_feedback


def calculate_ats_score(resume):
    """
    Calculates ATS Resume Score (/100)
    """

    score = 0
    section_scores = {}

    # ==========================
    # Contact Information
    # ==========================

    contact_score = 0

    if resume.name:
        contact_score += 2

    if resume.email:
        contact_score += 2

    if resume.phone:
        contact_score += 2

    if resume.linkedin:
        contact_score += 2

    if resume.github:
        contact_score += 2

    section_scores["contact"] = contact_score
    score += contact_score

    # ==========================
    # Skills
    # ==========================

    skills_score = min(len(resume.skills), SECTION_WEIGHTS["skills"])

    section_scores["skills"] = skills_score
    score += skills_score

    # ==========================
    # Education
    # ==========================

    education_score = (
        SECTION_WEIGHTS["education"]
        if resume.education
        else 0
    )

    section_scores["education"] = education_score
    score += education_score

    # ==========================
    # Experience
    # ==========================

    experience_score = (
        SECTION_WEIGHTS["experience"]
        if resume.experience
        else 0
    )

    section_scores["experience"] = experience_score
    score += experience_score

    # ==========================
    # Projects
    # ==========================

    project_score = (
        SECTION_WEIGHTS["projects"]
        if resume.projects
        else 0
    )

    section_scores["projects"] = project_score
    score += project_score

    # ==========================
    # Certifications
    # ==========================

    certification_score = (
        SECTION_WEIGHTS["certifications"]
        if resume.certifications
        else 0
    )

    section_scores["certifications"] = certification_score
    score += certification_score

    # ==========================
    # Keyword Matching
    # ==========================

    resume_text = " ".join(resume.skills).lower()

    matched_keywords = []
    missing_keywords = []

    for keyword in ALL_KEYWORDS:

        if keyword.lower() in resume_text:
            matched_keywords.append(keyword)
        else:
            missing_keywords.append(keyword)

    keyword_score = min(
        len(matched_keywords),
        SECTION_WEIGHTS["keywords"],
    )

    section_scores["keywords"] = keyword_score
    score += keyword_score

    # ==========================
    # Overall Score
    # ==========================

    score = min(score, 100)

    feedback = generate_feedback(score, section_scores)

    return {
        "score": score,
        "section_scores": section_scores,
        "matched_keywords": matched_keywords,
        "missing_keywords": missing_keywords,
        "feedback": feedback,
    }