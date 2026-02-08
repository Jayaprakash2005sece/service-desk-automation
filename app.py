from flask import Flask
from controllers.ticket_controller import ticket_bp
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.register_blueprint(ticket_bp, url_prefix="/api")

if __name__ == "__main__":
    app.run()
