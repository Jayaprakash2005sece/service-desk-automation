Service Desk Automation (O365 + ITSM)
Project Overview

This project implements a backend automation system that simulates how IT service desk tickets can be automatically created, classified, prioritized, assigned, and tracked using rule-based logic and REST APIs.

The solution focuses on real-world automation design rather than UI-heavy implementation, demonstrating strong backend engineering and workflow automation concepts.

Problem Statement

Traditional service desks rely on manual ticket creation and handling, which leads to:

Delayed ticket registration

Incorrect team assignment

SLA breaches

Reduced employee productivity

Lack of centralized tracking and visibility

Solution Overview

This project automates the complete IT service desk workflow:

Issues raised via O365 (Outlook / Teams) are processed automatically

Tickets are classified as Incident or Service Request

Priority and SLA are assigned dynamically

Tickets are routed to the appropriate support team

Users are notified instantly

External systems such as O365 and ITSM tools are simulated for lightweight execution

Key Features

Rule-based ticket classification

Automatic priority and SLA assignment

Keyword-based team routing

REST API–driven backend

Clean layered architecture

Easily extendable and scalable design

System Architecture

User (Outlook / Teams)
↓
Automation Service (Flask API)
↓
Rule Engine (Classification, SLA, Assignment)
↓
Mock ITSM Tool
↓
In-Memory Database

Automation Flow

User raises an issue via O365

Automation service receives the request

Issue details are extracted

Ticket is classified as Incident or Service Request

Priority and SLA are assigned

Ticket is routed to the correct support team

Ticket is created and tracked

User is notified

Technology Stack

Backend: Python (Flask)
API Style: REST
Data Storage: In-memory (extendable to SQLite or MySQL)
Tools: Postman, GitHub
