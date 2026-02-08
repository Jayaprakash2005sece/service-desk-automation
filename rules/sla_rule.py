def assign_sla(category, subject):
    subject = subject.lower()

    if category == "INCIDENT":
        if "down" in subject or "failed" in subject:
            return "HIGH", 4
        return "MEDIUM", 8

    return "LOW", 24
