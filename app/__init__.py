from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Config
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize DB
    db.init_app(app)

    # Register blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp)

    return app

