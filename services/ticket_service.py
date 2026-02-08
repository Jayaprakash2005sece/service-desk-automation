from rules.classification_rule import classify_ticket
from rules.assignment_rule import assign_team
from rules.sla_rule import assign_sla
from repository.ticket_repository import save_ticket

def create_ticket(data):
    subject = data.get("subject", "")
    description = data.get("description", "")

    category = classify_ticket(subject, description)
    priority, sla_hours = assign_sla(category, subject)
    team = assign_team(subject)

    ticket = {
        "subject": subject,
        "description": description,
        "category": category,
        "priority": priority,
        "assigned_team": team,
        "sla_hours": sla_hours,
        "status": "OPEN"
    }

    save_ticket(ticket)
    return ticket
