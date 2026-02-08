def assign_team(subject):
    subject = subject.lower()

    if "vpn" in subject:
        return "Network Team"
    if "email" in subject:
        return "IT Support"
    if "payroll" in subject:
        return "HR Tech"
    if "laptop" in subject:
        return "Asset Team"

    return "IT Support"
