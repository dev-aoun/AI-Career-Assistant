HIGH_PRIORITY = {
    "Python",
    "SQL",
    "Data Structures",
    "Algorithms",
    "Machine Learning",
    "Artificial Intelligence",
    "Cybersecurity",
    "Networking",
    "JavaScript",
}


def generate_learning_roadmap(missing_skills):

    roadmap = []

    for skill in missing_skills:

        if skill in HIGH_PRIORITY:
            priority = "High"

        elif skill in {
            "Git",
            "GitHub",
            "OOP",
            "Pandas",
            "NumPy",
            "REST API",
        }:
            priority = "Medium"

        else:
            priority = "Low"

        roadmap.append({
            "skill": skill,
            "priority": priority,
            "recommendation": (
                f"Learn {skill} through practical projects, "
                f"tutorials, and hands-on exercises."
            ),
        })

    priority_order = {
        "High": 1,
        "Medium": 2,
        "Low": 3,
    }

    roadmap.sort(
        key=lambda item: priority_order[item["priority"]]
    )

    return roadmap