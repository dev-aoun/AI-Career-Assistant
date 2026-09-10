def generate_feedback(match_score, matched_skills, missing_skills):

    if match_score >= 85:
        overall = (
            "Excellent match! Your resume strongly aligns "
            "with the selected job role."
        )

    elif match_score >= 70:
        overall = (
            "Good match. Your resume meets most of the "
            "required skills, but some improvements are recommended."
        )

    elif match_score >= 50:
        overall = (
            "Moderate match. You have several relevant skills, "
            "but should improve the missing skills before applying."
        )

    else:
        overall = (
            "Low match. Consider developing the missing skills "
            "to improve your suitability for this role."
        )

    suggestions = []

    if missing_skills:

        for skill in missing_skills:
            suggestions.append(
                f"Consider improving or learning {skill}."
            )

    if not matched_skills:
        suggestions.append(
            "Add relevant technical skills to your resume."
        )

    return {
        "overall": overall,
        "suggestions": suggestions
    }