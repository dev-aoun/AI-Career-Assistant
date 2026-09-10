from google import genai

from src.ai.config import AI_API_KEY, AI_MODEL


_client = None


def get_client():
    global _client

    if not AI_API_KEY:
        raise RuntimeError(
            "AI_API_KEY is not configured."
        )

    if _client is None:
        _client = genai.Client(
            api_key=AI_API_KEY
        )

    return _client


def generate_ai_response(prompt: str) -> str:

    client = get_client()

    response = client.models.generate_content(
        model=AI_MODEL,
        contents=prompt
    )

    return response.text.strip()