from dataclasses import dataclass, field


@dataclass
class ResumeData:
    # Personal Information
    name: str = ""
    email: str = ""
    phone: str = ""
    linkedin: str = ""
    github: str = ""
    location: str = ""

    # Resume Sections
    summary: list[str] = field(default_factory=list)
    education: list[str] = field(default_factory=list)
    experience: list[str] = field(default_factory=list)
    projects: list[str] = field(default_factory=list)
    skills: list[str] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    languages: list[str] = field(default_factory=list)

    # Calculated Information
    total_skills: int = 0
    total_projects: int = 0
    total_certifications: int = 0

    def finalize(self):
        self.skills = sorted(set(self.skills))
        self.projects = list(dict.fromkeys(self.projects))
        self.education = list(dict.fromkeys(self.education))
        self.experience = list(dict.fromkeys(self.experience))
        self.certifications = list(dict.fromkeys(self.certifications))

        self.total_skills = len(self.skills)
        self.total_projects = len(self.projects)
        self.total_certifications = len(self.certifications)

    def to_dict(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "linkedin": self.linkedin,
            "github": self.github,
            "location": self.location,
            "summary": self.summary,
            "education": self.education,
            "experience": self.experience,
            "projects": self.projects,
            "skills": self.skills,
            "certifications": self.certifications,
            "languages": self.languages,
            "total_skills": self.total_skills,
            "total_projects": self.total_projects,
            "total_certifications": self.total_certifications,
        }