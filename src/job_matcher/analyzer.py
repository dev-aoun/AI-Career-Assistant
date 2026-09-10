import re


def extract_skills_from_text(text, skill_database):
    """
    Extract known skills from job description text.
    Uses whole-word matching to avoid false matches.
    """

    text_lower = text.lower()

    found_skills = []

    for skill in skill_database:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return found_skills


def analyze_job_match(resume_skills, job_description, skill_database):
    """
    Compare resume skills against skills extracted from a job description.
    """

    required_skills = extract_skills_from_text(
        job_description,
        skill_database
    )

    resume_lower = {
        skill.lower()
        for skill in resume_skills
    }

    matched_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in resume_lower:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    return matched_skills, missing_skills, required_skills