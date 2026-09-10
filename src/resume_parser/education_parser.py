
import re


def parse_education(lines):
    """
    Parse education section into structured format.

    Each education entry contains:
        - degree
        - institution
        - duration
    """

    education = []

    current = None

    degree_pattern = re.compile(
        r"\b("
        r"Bachelor|Master|BS|MS|BSc|MSc|PhD|"
        r"Associate|Intermediate|Matric"
        r")\b",
        re.IGNORECASE
    )

    year_pattern = re.compile(
        r"\b(?:19|20)\d{2}\b"
    )

    for raw_line in lines:

        line = raw_line.strip()

        if not line:
            continue

        # Remove common bullet characters
        line = re.sub(r"^[•●▪◦\-]+\s*", "", line).strip()

        # Ignore relevant-course lines
        if re.match(
            r"^(Relevant Courses|Relevant Coursework|Coursework)\s*:",
            line,
            re.IGNORECASE
        ):
            continue

        # --------------------------------------------------
        # New degree / qualification
        # --------------------------------------------------

        if degree_pattern.search(line):

            if current:
                education.append(current)

            current = {
                "degree": line,
                "institution": "",
                "duration": ""
            }

            # Extract years directly from the degree line
            years = year_pattern.findall(line)

            if years:
                if "present" in line.lower():
                    current["duration"] = f"{years[0]} – Present"
                elif len(years) >= 2:
                    current["duration"] = f"{years[0]} – {years[1]}"
                else:
                    current["duration"] = years[0]

            continue

        # --------------------------------------------------
        # Institution
        # --------------------------------------------------

        if current and not current["institution"]:

            # Avoid treating coursework as institution
            if not re.match(
                r"^(Relevant Courses|Relevant Coursework|Coursework)",
                line,
                re.IGNORECASE
            ):
                current["institution"] = line

            continue

        # --------------------------------------------------
        # Duration
        # --------------------------------------------------

        if current and year_pattern.search(line):

            years = year_pattern.findall(line)

            if "present" in line.lower():
                if years:
                    current["duration"] = f"{years[0]} – Present"

            elif len(years) >= 2:
                current["duration"] = f"{years[0]} – {years[1]}"

            elif years:
                current["duration"] = years[0]

    # ------------------------------------------------------
    # Add final education entry
    # ------------------------------------------------------

    if current:
        education.append(current)

    return education