import re


def clean_text(text: str) -> str:
    """
    Clean extracted resume text.
    """

    # Normalize line endings
    text = text.replace("\r\n", "\n")
    text = text.replace("\r", "\n")

    # Normalize tabs
    text = text.replace("\t", " ")

    # Normalize bullets
    bullets = ["•", "●", "▪", "◦", "■", "►"]

    for bullet in bullets:
        text = text.replace(bullet, "- ")

    # Remove duplicate spaces
    text = re.sub(r"[ ]{2,}", " ", text)

    # Remove excessive blank lines
    text = re.sub(r"\n{3,}", "\n\n", text)

    return text.strip()


def split_lines(text: str):
    """
    Return clean non-empty lines.
    """

    return [
        line.strip()
        for line in text.split("\n")
        if line.strip()
    ]


def normalize(text: str) -> str:
    """
    Lowercase and remove extra spaces.
    """

    return re.sub(r"\s+", " ", text.lower()).strip()


def remove_duplicates(items):
    """
    Preserve order while removing duplicates.
    """

    seen = set()

    result = []

    for item in items:

        if item not in seen:

            result.append(item)

            seen.add(item)

    return result