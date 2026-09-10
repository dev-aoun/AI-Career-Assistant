from src.skill_gap.roles import ROLE_SKILLS


def analyze_skill_gap(resume_skills, target_role):

    required_skills = ROLE_SKILLS.get(target_role, [])

    resume_skills_lower = {
        skill.lower()
        for skill in resume_skills
    }

    current_skills = []
    missing_skills = []

    for skill in required_skills:

        if skill.lower() in resume_skills_lower:
            current_skills.append(skill)
        else:
            missing_skills.append(skill)

    total = len(required_skills)

    if total:
        completion = round(
            (len(current_skills) / total) * 100
        )
    else:
        completion = 0

    return {
        "target_role": target_role,
        "current_skills": current_skills,
        "missing_skills": missing_skills,
        "completion": completion,
    }