# 🤖 AI Career Assistant

An AI-powered career assistance web application built with **Python and Streamlit**.

The AI Career Assistant helps job seekers analyze their resumes, compare their skills with job requirements, identify skill gaps, and receive AI-powered career recommendations.

> **Current Release: Version 1.0**
> Version 1 focuses on the core resume analysis and career-assistance foundation. Advanced AI features and additional improvements are planned for Version 2.0.

---

## 📌 Table of Contents

* [Overview](#-overview)
* [Project Goals](#-project-goals)
* [Version 1.0 Features](#-version-10-features)
* [How the Application Works](#-how-the-application-works)
* [Technology Stack](#-technology-stack)
* [Project Structure](#-project-structure)
* [Requirements](#-requirements)
* [Installation](#-installation)
* [Environment Configuration](#-environment-configuration)
* [Running the Application](#-running-the-application)
* [Application Modules](#-application-modules)
* [Resume Parser](#-resume-parser)
* [Job Matcher](#-job-matcher)
* [Skill Gap Analyzer](#-skill-gap-analyzer)
* [AI Resume Analysis](#-ai-resume-analysis)
* [Supported Resume Information](#-supported-resume-information)
* [Testing](#-testing)
* [Example Workflow](#-example-workflow)
* [Version 1.0 Status](#-version-10-status)
* [Version 2.0 Roadmap](#-version-20-roadmap)
* [Limitations](#-limitations)
* [Security Notes](#-security-notes)
* [Future Improvements](#-future-improvements)
* [Author](#-author)
* [License](#-license)

---

# 📖 Overview

**AI Career Assistant** is a web-based career assistance application designed to help students, fresh graduates, junior developers, and job seekers better understand their resumes and career readiness.

The application provides several career-related tools through a simple Streamlit interface.

The current Version 1.0 focuses on:

* Resume parsing
* Contact information extraction
* Skills extraction
* Education extraction
* Project extraction
* Experience extraction
* Certification extraction
* Language extraction
* Job description matching
* Skill gap analysis
* Career roadmap generation
* AI-powered resume analysis

The application is designed to be expanded over time.

---

# 🎯 Project Goals

The main goals of the project are to:

1. Help users understand the information contained in their resumes.
2. Automatically extract important resume information.
3. Compare a user's skills with a target job description.
4. Identify missing skills.
5. Provide a learning roadmap for skill development.
6. Use AI to provide additional resume feedback.
7. Create a foundation for more advanced AI career-assistance features in future versions.

---

# ✨ Version 1.0 Features

## 📄 Resume Parser

Users can upload a resume and automatically extract information such as:

* Name
* Email
* Phone number
* LinkedIn
* GitHub
* Location
* Skills
* Education
* Projects
* Experience
* Certifications
* Languages

The parser supports resume files such as PDF and DOCX according to the implemented parser functionality.

---

## 🔍 Job Matcher

The Job Matcher compares the skills detected from the resume with skills required by a target job description.

It provides:

* Required skills
* Matching skills
* Missing skills
* Match percentage
* Basic feedback about the candidate's match

Example:

```text
Required Skills:
Python
SQL
Git
GitHub
OOP
Algorithms
Data Structures
Problem Solving

Matching Skills:
Python
SQL
GitHub
OOP
Algorithms
Data Structures

Missing Skills:
Git
Problem Solving
```

This helps users understand how closely their current skills align with a particular job.

---

## 📊 Skill Gap Analyzer

The Skill Gap Analyzer identifies skills that are missing from a user's current skill set.

It provides:

* Current skills
* Missing skills
* Completion percentage
* Skill priorities
* Learning roadmap

Example priorities may include:

```text
Git        → Medium Priority
Java       → Low Priority
C++        → Low Priority
Problem Solving → Low Priority
```

The purpose is to help users decide which skills they should focus on learning next.

---

## 🤖 AI Resume Analysis

Version 1.0 includes integration with Google's Gemini API.

The AI analyzes the parsed resume and provides career-oriented feedback.

The analysis can include:

* Resume strengths
* Resume weaknesses
* Areas that need improvement
* Recommendations
* Career suggestions
* Suggestions for improving projects or experience
* General resume quality feedback

The AI integration uses an API key stored in an environment variable rather than directly inside the source code.

---

# 🔄 How the Application Works

The general workflow is:

```text
                 ┌─────────────────────┐
                 │      User           │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Upload Resume       │
                 │ PDF / DOCX          │
                 └──────────┬──────────┘
                            │
                            ▼
                 ┌─────────────────────┐
                 │ Resume Extraction   │
                 └──────────┬──────────┘
                            │
                            ▼
              ┌─────────────────────────────┐
              │ Resume Parser               │
              │                             │
              │ • Contact                   │
              │ • Skills                    │
              │ • Education                 │
              │ • Projects                  │
              │ • Experience                │
              │ • Certifications            │
              │ • Languages                 │
              └──────────────┬──────────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
              ▼              ▼              ▼
        Job Matcher    Skill Gap       AI Analysis
              │              │              │
              ▼              ▼              ▼
        Match Result     Roadmap       AI Feedback
```

---

# 🛠 Technology Stack

## Programming Language

* **Python 3.11**

## Frontend / Web Interface

* **Streamlit**

## AI

* **Google Gemini API**
* Google GenAI Python SDK

## Resume Processing

* PDF text extraction
* DOCX document processing
* Custom Python parsing logic
* Regular expressions

## Development Tools

* Python virtual environment (`venv`)
* PowerShell
* Git / GitHub
* VS Code or another Python IDE

---

# 📁 Project Structure

```text
AI-Career-Assistant/
│
├── app.py
├── README.md
├── requirements.txt
├── Dockerfile
├── .gitignore
├── .dockerignore
├── .env
├── .env.example
├── project_tree.txt
│
├── assets/
│   └── styles.css
│
├── uploads/
│   └── resume files
│
├── src/
│   │
│   ├── ats_scorer/
│   │   └── scorer.py
│   │
│   ├── chatbot/
│   │   ├── chatbot.py
│   │   ├── responses.py
│   │   └── __init__.py
│   │
│   ├── components/
│   │   ├── cards.py
│   │   ├── footer.py
│   │   ├── header.py
│   │   ├── hero.py
│   │   ├── metrics.py
│   │   ├── sidebar.py
│   │   └── __init__.py
│   │
│   ├── cover_letter/
│   │   ├── generator.py
│   │   ├── templates.py
│   │   └── __init__.py
│   │
│   ├── interview/
│   │   ├── generator.py
│   │   ├── interview.py
│   │   ├── questions.py
│   │   └── __init__.py
│   │
│   ├── job_matcher/
│   │   ├── keywords.py
│   │   ├── matcher.py
│   │   └── __init__.py
│   │
│   ├── llm/
│   │
│   ├── pages/
│   │   ├── ats_score.py
│   │   ├── chatbot.py
│   │   ├── cover_letter.py
│   │   ├── home.py
│   │   ├── interview.py
│   │   ├── job_matcher.py
│   │   ├── resume_parser.py
│   │   ├── skill_gap.py
│   │   └── __init__.py
│   │
│   ├── resume_parser/
│   │   ├── contact.py
│   │   ├── education_parser.py
│   │   ├── experience_parser.py
│   │   ├── extractor.py
│   │   ├── models.py
│   │   ├── parser.py
│   │   ├── patterns.py
│   │   ├── project_parser.py
│   │   ├── section_parser.py
│   │   ├── skill_parser.py
│   │   ├── skills.py
│   │   ├── utils.py
│   │   └── __init__.py
│   │
│   ├── skill_gap/
│   │   ├── analyzer.py
│   │   ├── roadmap.py
│   │   └── __init__.py
│   │
│   └── utils/
│       └── theme.py
│
├── tests/
│   ├── test_parser.py
│   ├── test_resume_parser.py
│   └── ...
│
└── venv/
```

> The `venv` directory is a local Python virtual environment and should not be committed to GitHub.

---

# 📦 Requirements

The project requires:

* Python 3.11
* pip
* Internet connection for AI API requests
* A Gemini API key for AI features

Python 3.11 is currently the recommended environment for this project.

---

# ⚙️ Installation

## 1. Clone or download the project

Place the project somewhere on your computer.

Example:

```text
E:\AI-Career-Assistant
```

Open PowerShell and navigate to the project:

```powershell
cd E:\AI-Career-Assistant
```

---

## 2. Create a virtual environment

If a virtual environment does not already exist:

```powershell
python -m venv venv
```

---

## 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

After successful activation, the terminal should look similar to:

```text
(venv) PS E:\AI-Career-Assistant>
```

---

## 4. Install dependencies

Install the required packages:

```powershell
pip install -r requirements.txt
```

If `pip` causes environment confusion, use:

```powershell
python -m pip install -r requirements.txt
```

---

# 🔐 Environment Configuration

The project uses environment variables for configuration.

Create a `.env` file in the project root:

```text
E:\AI-Career-Assistant\.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

If the project configuration uses another variable name, use the name expected by the AI configuration module.

### Important

Never commit your actual `.env` file containing your API key to GitHub.

The `.gitignore` file should contain:

```gitignore
.env
venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Make sure the virtual environment is activated:

```powershell
.\venv\Scripts\Activate.ps1
```

Then start Streamlit:

```powershell
streamlit run app.py
```

If the `streamlit` command is not recognized, use:

```powershell
python -m streamlit run app.py
```

Streamlit will start a local web server.

You can then open the address shown in the terminal, normally similar to:

```text
http://localhost:8501
```

---

# 🖥️ Application Modules

The application contains multiple career-assistance modules.

Current and planned modules include:

| Module             |  Version 1 |       Version 2 |
| ------------------ | ---------: | --------------: |
| Home               |          ✅ |    Improvements |
| Resume Parser      |          ✅ |    Improvements |
| Job Matcher        |          ✅ | AI Improvements |
| Skill Gap          |          ✅ | AI Improvements |
| AI Resume Analysis |          ✅ |    Improvements |
| ATS Score          | Foundation |        Advanced |
| Cover Letter       | Foundation |      AI-powered |
| Interview          | Foundation |      AI-powered |
| Chatbot            | Foundation | AI improvements |

---

# 📄 Resume Parser

The Resume Parser is one of the main components of Version 1.0.

It processes an uploaded resume and attempts to identify important sections.

### Extracted information

```text
Personal Information
├── Name
├── Email
├── Phone
├── LinkedIn
├── GitHub
└── Location

Professional Information
├── Skills
├── Education
├── Experience
├── Projects
├── Certifications
└── Languages
```

The parser uses custom Python modules to process different parts of the resume.

---

# 🔎 Job Matcher

The Job Matcher is designed to compare resume skills with a target job description.

### Process

```text
Resume
   │
   ▼
Extract Skills
   │
   ▼
Enter Job Description
   │
   ▼
Extract Required Skills
   │
   ▼
Compare Skills
   │
   ├── Matching Skills
   ├── Missing Skills
   └── Match Percentage
```

The result helps users identify whether their current skill set matches the requirements of a particular position.

---

# 📊 Skill Gap Analyzer

The Skill Gap Analyzer uses the user's existing skills and identified missing skills.

It calculates an approximate completion level and organizes missing skills by priority.

Example:

```text
Current Skills
───────────────
Python
SQL
GitHub
OOP
Algorithms
Data Structures


Missing Skills
───────────────
Git
Java
C++
Problem Solving
```

A roadmap is then generated to help the user decide what to study.

---

# 🤖 AI Resume Analysis

The AI Resume Analysis feature connects the application to the Gemini API.

The general process is:

```text
Uploaded Resume
      │
      ▼
Resume Parser
      │
      ▼
Structured Resume Data
      │
      ▼
Gemini AI
      │
      ▼
Career Analysis
      │
      ├── Strengths
      ├── Weaknesses
      ├── Recommendations
      └── Improvement Suggestions
```

The AI does not replace the resume parser.

Instead:

```text
Parser → extracts structured information

AI → analyzes that information
```

This separation makes the application easier to maintain and expand.

---

# 🧪 Testing

The project contains tests for important parser functionality.

For example, the resume parser can be tested using:

```powershell
python -m tests.test_resume_parser
```

Running the test as a Python module helps ensure that the project's `src` package can be imported correctly.

---

# 🔄 Example Workflow

A typical Version 1 workflow looks like this:

### Step 1 — Start the application

```powershell
.\venv\Scripts\Activate.ps1
python -m streamlit run app.py
```

### Step 2 — Upload resume

The user uploads a PDF or DOCX resume.

### Step 3 — Parse resume

The system extracts:

* Contact information
* Skills
* Education
* Experience
* Projects
* Certifications
* Languages

### Step 4 — Review resume

The user reviews the extracted information.

### Step 5 — Analyze job match

The user enters a job description.

The system identifies:

* Required skills
* Matching skills
* Missing skills
* Match percentage

### Step 6 — Analyze skill gaps

The user can see which skills need improvement.

### Step 7 — Generate AI feedback

The user can request AI-powered resume analysis.

---

# ✅ Version 1.0 Status

Version 1.0 establishes the main foundation of the AI Career Assistant.

### Completed

* [x] Project structure
* [x] Python environment
* [x] Streamlit application
* [x] Resume upload
* [x] PDF resume extraction
* [x] DOCX resume extraction
* [x] Contact extraction
* [x] Email extraction
* [x] Phone extraction
* [x] GitHub extraction
* [x] LinkedIn extraction
* [x] Skills extraction
* [x] Education extraction
* [x] Experience extraction
* [x] Project extraction
* [x] Certification extraction
* [x] Language extraction
* [x] Job matching
* [x] Matching percentage
* [x] Missing skill identification
* [x] Skill gap analysis
* [x] Learning roadmap
* [x] Gemini API integration
* [x] AI resume analysis
* [x] Basic testing

---

# 🚀 Version 2.0 Roadmap

Version 2.0 will focus on making the application more intelligent, polished, and useful.

Planned improvements include:

## 🤖 Advanced AI Integration

* AI-powered job matching
* More detailed resume analysis
* Personalized career recommendations
* AI-powered skill-gap analysis
* Better contextual recommendations

---

## ✍️ AI Cover Letter Generator

Future versions can generate customized cover letters using:

```text
Resume
+
Job Description
+
User Information
        ↓
   AI Analysis
        ↓
Customized Cover Letter
```

---

## 🎤 AI Interview Preparation

Future interview functionality can include:

* Job-specific interview questions
* Technical questions
* Behavioral questions
* AI-generated answers
* Interview feedback
* Follow-up questions
* Interview scoring

---

## 💬 AI Career Chatbot

The chatbot can eventually become a complete career assistant capable of answering questions about:

* Career planning
* Resume improvement
* Job preparation
* Skills
* Interview preparation
* Learning paths
* Career transitions

---

## 📈 Advanced ATS Scoring

Future versions can provide a more comprehensive ATS score based on:

* Keywords
* Job-description relevance
* Resume structure
* Skills
* Experience
* Formatting
* Section completeness

---

## 🎨 UI/UX Improvements

Potential improvements include:

* Better dashboard
* Improved navigation
* Better charts
* More responsive design
* Improved resume result cards
* Better loading states
* Improved error messages
* Mobile-friendly interface

---

## 🗄️ Database and User Accounts

A future version may introduce:

* User accounts
* Resume history
* Saved job descriptions
* Saved analyses
* Career progress tracking
* Resume versions
* Persistent user data

---

## ☁️ Deployment

After development and testing, the application can be deployed to a cloud platform so users can access it through a public URL.

The deployment architecture may eventually look like:

```text
User
 │
 ▼
Internet
 │
 ▼
Hosted AI Career Assistant
 │
 ├── Streamlit
 ├── Python
 ├── AI API
 └── Database
```

---

# ⚠️ Limitations

Version 1.0 is intentionally a foundation release.

Some limitations include:

### Resume Parsing

Resume formatting varies significantly between documents.

Complex layouts, tables, columns, images, unusual fonts, or poorly structured PDFs may reduce extraction accuracy.

### LinkedIn

LinkedIn information may be extracted differently depending on how the resume represents the LinkedIn profile.

For example, a resume may contain:

```text
LinkedIn: Muhammad Aoun
```

instead of a complete profile URL.

### Skill Matching

The Job Matcher currently relies heavily on recognized skills and keywords.

Different wording or synonyms may not always be interpreted as equivalent.

### AI Analysis

AI-generated feedback can sometimes be incomplete or inaccurate.

Users should treat AI recommendations as assistance rather than guaranteed professional advice.

### Version Scope

Several advanced features are intentionally reserved for Version 2.0.

---

# 🔐 Security Notes

## API Keys

Never hard-code API keys into Python files.

Avoid:

```python
api_key = "YOUR_SECRET_KEY"
```

Use environment variables instead.

Example:

```env
GEMINI_API_KEY=your_api_key
```

---

## `.env`

The `.env` file should not be committed to GitHub.

Add:

```gitignore
.env
```

to `.gitignore`.

---

## Virtual Environment

The local virtual environment should also not be committed:

```gitignore
venv/
```

Other generated Python files should also be ignored:

```gitignore
__pycache__/
*.pyc
```

---

# 🧹 Development Guidelines

When extending the project:

1. Keep each feature in its own module.
2. Avoid putting all application logic inside `app.py`.
3. Keep parsing logic separate from UI code.
4. Keep AI integration separate from the UI.
5. Use environment variables for secrets.
6. Test parser changes before integrating them into the UI.
7. Make small changes and test frequently.
8. Keep Version 1 stable while developing Version 2.

---

# 📌 Development Philosophy

This project follows a gradual development approach:

```text
Version 1
   │
   ▼
Stable Foundation
   │
   ▼
Version 2
   │
   ▼
Advanced AI Features
   │
   ▼
Production Improvements
```

The goal is not to build every feature at once.

Instead, the project is developed incrementally so that each version provides a working application while creating a foundation for the next version.

---

# 🗺️ Long-Term Vision

The long-term goal is to evolve the project into a complete AI-powered career assistant.

The future application could provide:

```text
                    AI CAREER ASSISTANT
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
        ▼                  ▼                  ▼
     Resume             Jobs              Skills
     Analysis           Matching           Analysis
        │                  │                  │
        └──────────────────┼──────────────────┘
                           │
                           ▼
                    Career Guidance
                           │
             ┌─────────────┼─────────────┐
             │             │             │
             ▼             ▼             ▼
         Cover Letter   Interview      Career
          Generator     Preparation    Chatbot
```

The application can eventually become a centralized platform where users can manage their resume, evaluate job opportunities, identify missing skills, prepare for interviews, and receive personalized career guidance.

---

# 👨‍💻 Author

**Muhammad Aoun**

Computer Science Student / Junior Developer

Project:

**AI Career Assistant**

Built as a personal software development and AI learning project.

---

# 📜 License

This project can be adapted according to the licensing requirements chosen for the repository.

If a specific open-source license is selected later, this section should be updated accordingly.

---

# ⭐ Project Status

**Version 1.0 — Completed**

The core Version 1 foundation is complete.

Further development will continue under:

**Version 2.0 — Advanced AI Career Assistant**

---

## 📝 Final Note

This project is continuously evolving.

Version 1 focuses on building a reliable foundation for:

**Resume → Skills → Job Matching → Skill Gap → AI Analysis**

Version 2 will build on this foundation with more advanced AI capabilities, improved user experience, and additional career-assistance tools.
