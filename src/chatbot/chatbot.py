from src.chatbot.responses import RESPONSES


def chatbot_response(message):

    message = message.lower()

    if "resume" in message:
        return RESPONSES["resume"]

    elif "ats" in message:
        return RESPONSES["ats"]

    elif "interview" in message:
        return RESPONSES["interview"]

    elif "skill" in message:
        return RESPONSES["skills"]

    elif "career" in message or "job" in message:
        return RESPONSES["career"]

    return (
        "🤖 I can help with resumes, ATS optimization, interview preparation, "
        "skills, and career advice. Try asking about one of those topics."
    )