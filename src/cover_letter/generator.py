from src.cover_letter.templates import TEMPLATES


def generate_cover_letter(
    name,
    position,
    skills,
    experience,
    tone="Professional",
):
    """
    Generate a cover letter using the selected template.
    """

    template = TEMPLATES.get(tone, TEMPLATES["Professional"])

    cover_letter = template.format(
        name=name,
        position=position,
        skills=skills,
        experience=experience,
    )

    return cover_letter