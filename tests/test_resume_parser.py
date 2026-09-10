from src.resume_parser.parser import parse_resume_file

resume = parse_resume_file("uploads/M Aoun CV.pdf")

print("=" * 60)

print("Name:", resume.name)
print("Email:", resume.email)
print("Phone:", resume.phone)
print("LinkedIn:", resume.linkedin)
print("GitHub:", resume.github)

print("\nSkills")
print(resume.skills)

print("\nEducation")
print(resume.education)

print("\nProjects")
print(resume.projects)

print("\nExperience")
print(resume.experience)

print("\nCertifications")
print(resume.certifications)

print("\nLanguages")
print(resume.languages)