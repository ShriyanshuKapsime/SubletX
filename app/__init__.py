from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # ===== CONFIG =====
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'supersecretkey123'  # 🔑 Required for session login

    # ===== INITIALIZE DB =====
    db.init_app(app)

    # ===== REGISTER BLUEPRINTS =====
    from app.routes.user_routes import user_bp
    from app.routes.listing_routes import listing_bp
    from app.routes.transaction_routes import transaction_bp
    from app.routes.auth_routes import auth_bp

    app.register_blueprint(auth_bp)         # must register first since /auth is prefix
    app.register_blueprint(user_bp)
    app.register_blueprint(listing_bp)
    app.register_blueprint(transaction_bp)

    return app
