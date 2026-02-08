tickets_db = []

def save_ticket(ticket):
    tickets_db.append(ticket)

def get_all_tickets():
    return tickets_db
