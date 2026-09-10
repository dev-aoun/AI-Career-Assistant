import re

from src.resume_parser.skills import SKILLS


# ==========================================================
# Normalize Skills
# ==========================================================

SKILL_SYNONYMS = {
    "oop": "Object-Oriented Programming",
    "object oriented programming": "Object-Oriented Programming",
    "object-oriented programming": "Object-Oriented Programming",
    "ai": "Artificial Intelligence",
    "ml": "Machine Learning",
    "js": "JavaScript",
    "ts": "TypeScript",
    "py": "Python",
}


# ==========================================================
# Extract Skills
# ==========================================================

def extract_skills(text: str):
    """
    Extract technical skills using longest-match-first.
    """

    text = text.lower()

    found = []

    # Longest skill names first
    ordered_skills = sorted(SKILLS, key=len, reverse=True)

    for skill in ordered_skills:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text):
            found.append(skill)

    # Synonyms

    for short_name, original in SKILL_SYNONYMS.items():

        pattern = r"\b" + re.escape(short_name) + r"\b"

        if re.search(pattern, text):

            if original not in found:
                found.append(original)

    return sorted(set(found))


# ==========================================================
# Count Skill Frequency
# ==========================================================

def skill_frequency(text: str):

    text = text.lower()

    frequency = {}

    for skill in SKILLS:

        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        matches = re.findall(pattern, text)

        if matches:

            frequency[skill] = len(matches)

    return frequency


# ==========================================================
# Skill Categories
# ==========================================================

SKILL_CATEGORIES = {

    "Programming": [
        "Python",
        "Java",
        "C",
        "C++",
        "JavaScript",
    ],

    "Database": [
        "SQL",
        "MySQL",
        "MongoDB",
        "PostgreSQL",
    ],

    "AI": [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "NLP",
    ],

    "Web": [
        "HTML",
        "CSS",
        "React",
        "Flask",
        "Django",
        "FastAPI",
    ],

    "Cloud": [
        "AWS",
        "Azure",
        "GCP",
    ],

    "DevOps": [
        "Docker",
        "Kubernetes",
        "Git",
        "GitHub",
    ],

    "Networking": [
        "Networking",
        "TCP/IP",
        "DNS",
        "HTTP",
    ],

    "Cybersecurity": [
        "Cybersecurity",
        "Ethical Hacking",
        "OWASP",
    ]
}


# ==========================================================
# Categorize Skills
# ==========================================================

def categorize_skills(skills):

    result = {}

    for category, category_skills in SKILL_CATEGORIES.items():

        matched = []

        for skill in skills:

            if skill in category_skills:
                matched.append(skill)

        if matched:

            result[category] = matched

    return result