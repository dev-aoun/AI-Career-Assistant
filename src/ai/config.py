import os

from dotenv import load_dotenv

load_dotenv()

AI_API_KEY = os.getenv("AI_API_KEY", "")

AI_MODEL = os.getenv(
    "AI_MODEL",
    "gemini-2.5-flash"
)