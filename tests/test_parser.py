from src.resume_parser.parser import extract_text_from_pdf

from src.resume_parser.extractor import (
    extract_name,
    extract_email,
    extract_phone,
    extract_skills,
)

resume = "uploads/resume.pdf"

text = extract_text_from_pdf(resume)

print("\n========== Resume Information ==========\n")

print("Name :", extract_name(text))
print("Email:", extract_email(text))
print("Phone:", extract_phone(text))

print("\nSkills Found:\n")

for skill in extract_skills(text):
    print("✓", skill)