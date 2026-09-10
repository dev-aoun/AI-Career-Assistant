from src.resume_parser.patterns import SECTION_HEADERS
from src.resume_parser.utils import normalize, split_lines


def parse_sections(text: str):
    """
    Split the resume into logical sections.

    Handles normal headings such as:
        EDUCATION
        EXPERIENCE
        PROJECTS

    Also handles combined headings such as:
        PROJECTS AND TECHNICAL EXPERIENCE
    """

    lines = split_lines(text)

    sections = {}

    current_section = "general"

    sections[current_section] = []

    # ------------------------------------------------------
    # Build heading lookup table
    # ------------------------------------------------------

    heading_lookup = {}

    for section_name, headings in SECTION_HEADERS.items():

        for heading in headings:
            heading_lookup[normalize(heading)] = section_name

    # ------------------------------------------------------
    # Additional / combined headings
    # ------------------------------------------------------

    combined_headings = {
        "projects and technical experience": "projects",
        "project and technical experience": "projects",
        "projects technical experience": "projects",
    }

    heading_lookup.update(combined_headings)

    # ------------------------------------------------------
    # Parse resume
    # ------------------------------------------------------

    for line in lines:

        key = normalize(line)

        # --------------------------------------------------
        # Normal or combined section heading
        # --------------------------------------------------

        if key in heading_lookup:

            current_section = heading_lookup[key]

            if current_section not in sections:
                sections[current_section] = []

            continue

        sections[current_section].append(line)

    # ------------------------------------------------------
    # Split IT Support from combined Projects section
    # ------------------------------------------------------

    if "projects" in sections:

        project_lines = []
        experience_lines = []

        in_experience = False

        experience_start_patterns = (
            "it support and software installation",
            "it support",
            "freelance",
            "self-initiated",
        )

        for line in sections["projects"]:

            normalized_line = normalize(line)

            # Detect the beginning of the IT Support experience
            if any(
                normalized_line.startswith(pattern)
                for pattern in experience_start_patterns
            ):
                in_experience = True

            if in_experience:
                experience_lines.append(line)
            else:
                project_lines.append(line)

        sections["projects"] = project_lines

        if experience_lines:

            if "experience" in sections:
                sections["experience"].extend(experience_lines)
            else:
                sections["experience"] = experience_lines

    return sections
