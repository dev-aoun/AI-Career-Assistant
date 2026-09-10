from src.resume_parser.models import ResumeData

from src.resume_parser.utils import clean_text
from src.resume_parser.contact import (
    extract_name,
    extract_email,
    extract_phone,
    extract_github,
    extract_linkedin,
)

from src.resume_parser.section_parser import parse_sections
from src.resume_parser.skill_parser import extract_skills
from src.resume_parser.education_parser import parse_education
from src.resume_parser.experience_parser import parse_experience
from src.resume_parser.project_parser import parse_projects

from src.resume_parser.utils import remove_duplicates


def parse_resume(text: str) -> ResumeData:
    """
    Main resume parser.
    """

    text = clean_text(text)

    sections = parse_sections(text)

    resume = ResumeData()

    # -------------------------
    # Contact
    # -------------------------

    resume.name = extract_name(text)
    resume.email = extract_email(text)
    resume.phone = extract_phone(text)
    resume.linkedin = extract_linkedin(text)
    resume.github = extract_github(text)

    # -------------------------
    # Skills
    # -------------------------

    resume.skills = remove_duplicates(
        extract_skills(
            "\n".join(sections.get("skills", [])) + "\n" + text
        )
    )

    # -------------------------
    # Education
    # -------------------------

    resume.education = parse_education(
        sections.get("education", [])
    )

    # -------------------------
    # Experience
    # -------------------------

    resume.experience = parse_experience(
        sections.get("experience", [])
    )

    # -------------------------
    # Projects
    # -------------------------

    resume.projects = parse_projects(
        sections.get("projects", [])
    )

    # -------------------------
    # Certifications
    # -------------------------

    resume.certifications = remove_duplicates(
        sections.get("certifications", [])
    )

    # -------------------------
    # Languages
    # -------------------------

    resume.languages = remove_duplicates(
        sections.get("languages", [])
    )

    return resume