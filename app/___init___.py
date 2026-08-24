from flask import Flask
from app.routes import tickets_bp


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    app.register_blueprint(tickets_bp)

    return app