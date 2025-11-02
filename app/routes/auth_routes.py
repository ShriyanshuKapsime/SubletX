from flask import Blueprint, request, jsonify
from app.models.user import User

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # --- For GET requests (for testing or browser access) ---
    if request.method == 'GET':
        return jsonify({
            "message": "Use POST method to log in.",
            "example_body": {
                "email": "anand@example.com",
                "password": "pass123"
            }
        }), 200

    # --- For POST requests ---
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()

    if user and user.check_password(password):
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role
            }
        }), 200
    else:
        return jsonify({"error": "Invalid credentials"}), 401
