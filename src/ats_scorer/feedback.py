# ==========================================
# ATS Feedback Generator
# ==========================================

from src.ats_scorer.rules import SECTION_WEIGHTS


def generate_feedback(score: int, section_scores: dict) -> dict:
    """
    Generates strengths, weaknesses and suggestions
    based on ATS score.
    """

    strengths = []
    weaknesses = []
    suggestions = []

    # --------------------------------------
    # Overall Score
    # --------------------------------------

    if score >= 90:
        overall = "Excellent ATS-ready resume."
    elif score >= 75:
        overall = "Good resume with minor improvements needed."
    elif score >= 60:
        overall = "Average resume. Several improvements recommended."
    else:
        overall = "Resume needs significant improvement."

    # --------------------------------------
    # Section Feedback
    # --------------------------------------

    for section, weight in SECTION_WEIGHTS.items():

        obtained = section_scores.get(section, 0)

        if obtained >= weight:
            strengths.append(f"{section.title()} section is complete.")
        else:
            weaknesses.append(f"{section.title()} section is incomplete.")

            suggestions.append(
                f"Improve your {section.replace('_', ' ')} section."
            )

    # Remove duplicate suggestions
    suggestions = list(dict.fromkeys(suggestions))

    return {
        "overall": overall,
        "strengths": strengths,
        "weaknesses": weaknesses,
        "suggestions": suggestions,
    }