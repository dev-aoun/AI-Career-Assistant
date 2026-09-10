import pdfplumber
import docx

from src.resume_parser.extractor import parse_resume


# ==========================================================
# PDF
# ==========================================================

def extract_text_from_pdf(file_path: str) -> str:

    text = ""

    with pdfplumber.open(file_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()

            if page_text:

                text += page_text + "\n"

    return text


# ==========================================================
# DOCX
# ==========================================================

def extract_text_from_docx(file_path: str) -> str:

    document = docx.Document(file_path)

    return "\n".join(
        paragraph.text
        for paragraph in document.paragraphs
    )


# ==========================================================
# MAIN PARSER
# ==========================================================

def parse_resume_file(file_path: str):

    if file_path.lower().endswith(".pdf"):

        text = extract_text_from_pdf(file_path)

    elif file_path.lower().endswith(".docx"):

        text = extract_text_from_docx(file_path)

    else:

        raise ValueError("Unsupported file format.")

    return parse_resume(text)