def classify_ticket(subject, description):
    keywords = ["error", "issue", "not working", "failed"]

    text = (subject + " " + description).lower()

    for word in keywords:
        if word in text:
            return "INCIDENT"

    return "SERVICE_REQUEST"
