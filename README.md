# **Service Desk Automation (O365 + ITSM)**

## **Project Overview**

A backend automation system that simulates how IT service desk tickets can be automatically created, classified, prioritized, assigned, and tracked using rule-based logic and REST APIs.

This project demonstrates real-world automation thinking rather than UI-heavy implementation.

## **Problem Statement**

Traditional service desks rely on manual ticket creation, which leads to:

→ **Delayed ticket registration**  
→ **Incorrect team assignment**  
→ **SLA breaches**  
→ **Reduced employee productivity**  
→ **No centralized tracking of incidents and SLAs**

## **Solution Overview**

This project automates the end-to-end service desk workflow:

→ **Issues raised via O365 (Outlook / Teams) are processed automatically**  
→ **Tickets are classified as Incident or Service Request**  
→ **Priority and SLA are assigned**  
→ **Tickets are routed to the correct support team**  
→ **Users are notified instantly**

External systems like O365 and ITSM tools are simulated to keep the solution lightweight and interview-focused.

## **Key Features**

→ **Rule-based ticket classification**  
→ **Automatic priority and SLA assignment**  
→ **Keyword-based team routing**  
→ **REST API–driven backend**  
→ **Clean layered architecture**  
→ **Easy to extend and scale**

## **System Architecture**

**User (Outlook / Teams)**  
            ↓  
**Automation Service (Flask API)**  
            ↓  
**Rule Engine (Classification, SLA, Assignment)**  
            ↓  
**ITSM Tool (Mocked)**  
            ↓  
**In-Memory Database**


## **Tech Stack**
→ **Backend:** Python (Flask)  
→ **API Style:** REST  
→ **Data Storage:** In-memory (extendable to SQLite / MySQL)  
→ **Tools:** Postman, GitHub  
→ **Backend:** Python (Flask)  
→ **API Style:** REST  
→ **Data Storage:** In-memory (extendable to SQLite / MySQL)  
→ **Tools:** Postman, GitHub  
