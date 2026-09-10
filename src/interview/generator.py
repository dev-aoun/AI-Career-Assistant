from src.interview.questions import QUESTIONS


def generate_questions(role, interview_type):
    """
    Generate interview questions based on role and interview type.
    interview_type can be:
    - HR
    - Technical
    - Mixed
    """

    if role not in QUESTIONS:
        return []

    role_questions = QUESTIONS[role]

    if interview_type == "HR":
        return role_questions["HR"]

    elif interview_type == "Technical":
        return role_questions["Technical"]

    elif interview_type == "Mixed":
        return role_questions["HR"] + role_questions["Technical"]

    return []