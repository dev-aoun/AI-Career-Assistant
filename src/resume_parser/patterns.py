import re


# ==========================================================
# EMAIL
# ==========================================================

EMAIL_PATTERN = re.compile(
    r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
)


# ==========================================================
# PHONE
# ==========================================================
# Supports:
# +923-187539-130
# +92 318 7539130
# +92-318-7539130
# 03187539130
# 0318-7539130
# (0318) 7539130

PHONE_PATTERN = re.compile(
    r"(\+92[\d\- ]{10,15}|0\d{3}[\- ]?\d{7})"
)


# ==========================================================
# LINKEDIN
# ==========================================================

LINKEDIN_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+",
    re.IGNORECASE
)


# ==========================================================
# GITHUB
# ==========================================================

GITHUB_PATTERN = re.compile(
    r"(?:https?://)?(?:www\.)?github\.com/[A-Za-z0-9_-]+",
    re.IGNORECASE
)


# ==========================================================
# SECTION HEADINGS
# ==========================================================

SECTION_HEADERS = {

    "education": [
        "education",
        "academic background",
        "academic qualification",
        "qualifications",
    ],

    "experience": [
        "experience",
        "work experience",
        "professional experience",
        "professional experience",
        "employment",
        "employment history",
        "technical experience",
        "professional and technical experience",
    ],

    "projects": [
        "projects",
        "project",
        "academic projects",
        "technical projects",
        "project experience",
        "projects and technical experience",
    ],

    "skills": [
        "skills",
        "technical skills",
        "core skills",
        "core technical skills",
        "technologies",
    ],

    "certifications": [
        "certifications",
        "certificates",
        "licenses",
        "training",
    ],

    "languages": [
        "languages",
        "language",
    ],
}