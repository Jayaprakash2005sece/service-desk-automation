class Ticket:
    def __init__(self, subject, description, category, priority, team, sla):
        self.subject = subject
        self.description = description
        self.category = category
        self.priority = priority
        self.assigned_team = team
        self.sla_hours = sla
        self.status = "OPEN"
