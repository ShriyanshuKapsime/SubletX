from flask import Blueprint, jsonify, render_template, request
from app import db
from app.models.user import User
from app.models.listing import Listing
# from app.models.transaction import Transaction  # Uncomment when you implement rentals

user_bp = Blueprint('user_bp', __name__)

# 🏠 Home Page
@user_bp.route('/', methods=['GET'])
def home():
    return render_template("index.html")


# 🌍 Browse Page
@user_bp.route("/browse", methods=['GET'])
def browse():
    return render_template("browse.html")


# 🧾 Listing Page
@user_bp.route("/listing", methods=['GET'])
def listing():
    return render_template("listing.html")


# 👤 Profile Page (HTML)
@user_bp.route('/profile', methods=['GET'])
def profile():
    return render_template("profile.html")


# 👤 Profile Data API (JSON for profile.js)
@user_bp.route('/api/profile', methods=['GET'])
def api_profile():
    # For now, hardcode user until login/session system exists
    user = User.query.filter_by(id="SELLER_ANAND").first()

    if not user:
        return jsonify({"error": "User not found"}), 404

    # Get listings created by the user
    listings = Listing.query.filter_by(user_id=user.id).all()

    # Rentals will be added later (empty list for now)
    rentals = []

    return jsonify({
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "role": user.role
        },
        "listings": [l.to_dict() for l in listings],
        "rentals": rentals
    })


# 👥 Route to get all users (for debugging)
@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])

