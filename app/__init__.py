import os

from app.extensions import db

from dotenv import load_dotenv
from flask import Flask
from app.routes import tickets_bp

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config["SQLALCHEMY_TRACK_MOTIFICATION"] = False

    db.init_app(app)

    @app.get("/health")
    def health():
        return {"status": "healthy"}

    app.register_blueprint(tickets_bp)

    return app