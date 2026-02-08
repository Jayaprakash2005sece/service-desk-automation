# Service Desk Automation (O365 + ITSM)

This project demonstrates a backend automation service that simulates how
issues raised via O365 (Outlook/Teams) can be automatically processed and
converted into ITSM tickets.

## Features
- Rule-based ticket classification
- Automatic priority & SLA assignment
- Auto-routing to support teams
- REST API based design

## Sample API

POST /api/tickets

Request:
{
  "subject": "VPN not working",
  "description": "Unable to connect to VPN"
}

Response:
{
  "category": "INCIDENT",
  "priority": "HIGH",
  "assigned_team": "Network Team",
  "sla_hours": 4
}
