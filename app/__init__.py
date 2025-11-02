# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Secret key (needed for sessions, CSRF, etc.)
    app.secret_key = "supersecretkey"

    # Database configuration
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize database
    db.init_app(app)

    # Import and register blueprints
    from app.routes.user_routes import user_bp
    from app.routes.listing_routes import listing_bp
    from app.routes.transaction_routes import transaction_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(transaction_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(listing_bp)

    # Create tables if not exist
    with app.app_context():
        db.create_all()

    return app
