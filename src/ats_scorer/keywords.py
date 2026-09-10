# ==========================================
# ATS Keywords Database
# ==========================================

COMMON_KEYWORDS = {

    "Programming": [
        "Python",
        "Java",
        "C",
        "C++",
        "C#",
        "JavaScript",
        "TypeScript",
        "Go",
        "Rust",
        "PHP",
    ],

    "Web Development": [
        "HTML",
        "CSS",
        "Bootstrap",
        "React",
        "Angular",
        "Vue",
        "Node.js",
        "Express",
        "Django",
        "Flask",
        "FastAPI",
        "Streamlit",
    ],

    "Databases": [
        "SQL",
        "MySQL",
        "PostgreSQL",
        "SQLite",
        "MongoDB",
        "Oracle",
    ],

    "Data Science": [
        "NumPy",
        "Pandas",
        "Matplotlib",
        "Seaborn",
        "Scikit-learn",
        "TensorFlow",
        "PyTorch",
    ],

    "AI & LLM": [
        "Artificial Intelligence",
        "Machine Learning",
        "Deep Learning",
        "NLP",
        "LLM",
        "LangChain",
        "RAG",
        "OpenAI",
        "Gemini",
    ],

    "Cloud & DevOps": [
        "Docker",
        "Kubernetes",
        "AWS",
        "Azure",
        "GCP",
        "Git",
        "GitHub",
        "CI/CD",
    ],

    "Networking": [
        "TCP/IP",
        "Networking",
        "Cybersecurity",
        "Linux",
        "Windows",
    ],

    "Soft Skills": [
        "Communication",
        "Leadership",
        "Problem Solving",
        "Critical Thinking",
        "Teamwork",
        "Time Management",
        "Project Management",
    ]
}


# ==========================================
# Flatten All Keywords
# ==========================================

ALL_KEYWORDS = []

for category in COMMON_KEYWORDS.values():
    ALL_KEYWORDS.extend(category)

ALL_KEYWORDS = sorted(set(ALL_KEYWORDS))