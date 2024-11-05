from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    CORS(app)

    from .routes import api_bp, home_bp
    app.register_blueprint(home_bp)
    app.register_blueprint(api_bp)

    return app
