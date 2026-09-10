from src.ai.client import generate_ai_response


def analyze_resume_with_ai(resume):

    prompt = f"""
You are a professional career and resume expert.

Analyze the following parsed resume.

Name:
{resume.name}

Skills:
{", ".join(resume.skills)}

Education:
{resume.education}

Experience:
{resume.experience}

Projects:
{resume.projects}

Certifications:
{", ".join(resume.certifications)}

Languages:
{", ".join(resume.languages)}

Provide:

1. 💪 Strengths
2. ⚠️ Weaknesses
3. 🚀 Improvement Recommendations

Keep the response practical and concise.
Do not invent experience, education, projects, or skills that are not present.
"""

    return generate_ai_response(prompt)