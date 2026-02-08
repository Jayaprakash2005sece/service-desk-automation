from flask import Blueprint, request, jsonify
from services.ticket_service import create_ticket

ticket_bp = Blueprint("ticket_bp", __name__)

@ticket_bp.route("/tickets", methods=["POST"])
def create_ticket_api():
    data = request.get_json()

    if not data or "subject" not in data:
        return jsonify({"error": "Invalid request"}), 400

    ticket = create_ticket(data)
    return jsonify(ticket), 201
