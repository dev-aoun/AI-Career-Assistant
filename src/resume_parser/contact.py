
import re

from src.resume_parser.patterns import (
    EMAIL_PATTERN,
    PHONE_PATTERN,
    LINKEDIN_PATTERN,
    GITHUB_PATTERN,
)

from src.resume_parser.utils import split_lines


# ==========================================================
# NAME
# ==========================================================

def extract_name(text: str) -> str:

    lines = split_lines(text)

    for line in lines[:5]:

        if "@" in line:
            continue

        if "linkedin" in line.lower():
            continue

        if "github" in line.lower():
            continue

        if any(char.isdigit() for char in line):
            continue

        words = line.split()

        if 2 <= len(words) <= 4:
            return line.strip()

    return ""


# ==========================================================
# EMAIL
# ==========================================================

def extract_email(text: str) -> str:

    match = EMAIL_PATTERN.search(text)

    return match.group(0) if match else ""


# ==========================================================
# PHONE
# ==========================================================

def extract_phone(text: str) -> str:

    match = PHONE_PATTERN.search(text)

    if match:
        return match.group(0)

    return ""


# ==========================================================
# LINKEDIN
# ==========================================================

def extract_linkedin(text: str) -> str:

    match = LINKEDIN_PATTERN.search(text)

    if match:
        return match.group(0)

    match = re.search(
        r"LinkedIn\s*:\s*([^\n|]+)",
        text,
        re.IGNORECASE
    )

    if match:
        return match.group(1).strip()

    return ""


# ==========================================================
# GITHUB
# ==========================================================

def extract_github(text: str) -> str:

    match = GITHUB_PATTERN.search(text)

    if match:
        return match.group(0)

    return ""


# ==========================================================
# LOCATION
# ==========================================================

def extract_location(text: str) -> str:

    city_patterns = [
        r"Lahore",
        r"Karachi",
        r"Islamabad",
        r"Rawalpindi",
        r"Faisalabad",
        r"Pakistan",
    ]

    for pattern in city_patterns:

        match = re.search(
            pattern,
            text,
            re.IGNORECASE
        )

        if match:
            return match.group(0)

    return ""
