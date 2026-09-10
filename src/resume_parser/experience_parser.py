import re


def parse_experience(lines):
    """
    Parse experience section into structured format.

    Groups:
    - Job title
    - Duration
    - Company / organization
    - Description
    """

    experiences = []

    current = None

    date_pattern = r"(19|20)\d{2}\s*[–-]\s*(Present|(19|20)\d{2})"

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # --------------------------------------------------
        # Detect a new experience title
        # --------------------------------------------------

        if (
            len(line) < 80
            and not line.startswith("-")
            and not line.startswith("•")
            and re.search(
                r"(Support|Developer|Engineer|Intern|Manager|Assistant|"
                r"Technician|Specialist|Analyst|Administrator)",
                line,
                re.I,
            )
            and not re.search(date_pattern, line)
        ):

            if current:
                experiences.append(current)

            current = {
                "title": line,
                "duration": "",
                "company": "",
                "description": [],
            }

        # --------------------------------------------------
        # Detect title containing duration
        # --------------------------------------------------

        elif re.search(date_pattern, line, re.I):

            if current is None:
                current = {
                    "title": "",
                    "duration": "",
                    "company": "",
                    "description": [],
                }

            match = re.search(date_pattern, line, re.I)

            if match:
                current["duration"] = match.group(0)

                title = re.sub(
                    date_pattern,
                    "",
                    line,
                    flags=re.I
                ).strip()

                if title:
                    current["title"] = title

        # --------------------------------------------------
        # Company / organization
        # --------------------------------------------------

        elif (
            current
            and not current["company"]
            and len(line) < 70
            and not line.startswith("-")
            and not line.startswith("•")
        ):

            current["company"] = line

        # --------------------------------------------------
        # Description
        # --------------------------------------------------

        else:

            if current:
                current["description"].append(line)

    # Add final experience
    if current:
        experiences.append(current)

    return experiences