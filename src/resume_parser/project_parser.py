
import re


def parse_projects(lines):
    """
    Parse projects into structured format.

    A project title is identified by:
    - A reasonably short line
    - Usually containing a project-related keyword
    - Or containing a year
    - Bullet points are kept as descriptions
    """

    projects = []

    current = None

    project_title_pattern = re.compile(
        r"(project|system|algorithm|application|database|website|"
        r"app|platform|management|development)",
        re.IGNORECASE
    )

    year_pattern = re.compile(
        r"\b(?:19|20)\d{2}\b"
    )

    bullet_pattern = re.compile(
        r"^[\-•●▪◦]\s*"
    )

    for raw_line in lines:

        line = raw_line.strip()

        if not line:
            continue

        # Remove PDF bullet characters
        clean_line = bullet_pattern.sub("", line).strip()

        # --------------------------------------------------
        # Ignore obvious institution/course lines
        # --------------------------------------------------

        if clean_line.lower().startswith(
            (
                "semester project",
                "course project",
                "database management systems",
                "bahria university - artificial intelligence",
            )
        ):
            if current:
                current["description"].append(clean_line)
            continue

        # --------------------------------------------------
        # Detect project title
        # --------------------------------------------------

        is_title = (
            len(clean_line) < 100
            and (
                project_title_pattern.search(clean_line)
                or year_pattern.search(clean_line)
            )
            and not bullet_pattern.match(line)
        )

        if is_title:

            if current:
                projects.append(current)

            current = {
                "title": clean_line,
                "description": []
            }

            continue

        # --------------------------------------------------
        # Description
        # --------------------------------------------------

        if current:
            current["description"].append(clean_line)

    if current:
        projects.append(current)

    return projects
