from src.job_matcher.analyzer import analyze_job_match
from src.job_matcher.keywords import ROLE_SKILLS
from src.job_matcher.feedback import generate_feedback


# Build one combined skill database
ALL_JOB_SKILLS = []

for skills in ROLE_SKILLS.values():
    ALL_JOB_SKILLS.extend(skills)

ALL_JOB_SKILLS = sorted(set(ALL_JOB_SKILLS))


def calculate_job_match(resume, job_description):

    matched_skills, missing_skills, required_skills = analyze_job_match(
        resume.skills,
        job_description,
        ALL_JOB_SKILLS
    )

    total_required = len(required_skills)

    if total_required == 0:
        score = 0
    else:
        score = round(
            (len(matched_skills) / total_required) * 100
        )

    feedback = generate_feedback(
        score,
        matched_skills,
        missing_skills
    )

    return {
        "match_score": score,
        "required_skills": required_skills,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "feedback": feedback,
    }