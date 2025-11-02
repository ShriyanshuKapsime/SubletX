from flask import Blueprint, jsonify, render_template, request, session
from app import db
from app.models.user import User
from app.models.listing import Listing

user_bp = Blueprint("user_bp", __name__)

# 🏠 Home Page
@user_bp.route("/", methods=["GET"])
def home():
    return render_template("index.html")


# 🌍 Browse Page
@user_bp.route("/browse", methods=["GET"])
def browse():
    return render_template("browse.html")


# 🧾 Listing Page
@user_bp.route("/listing", methods=["GET"])
def listing():
    return render_template("listing.html")


# 👤 Profile Page (renders HTML)
@user_bp.route("/profile", methods=["GET"])
def profile():
    # Ensure user is logged in
    user_id = session.get("user_id")
    if not user_id:
        return render_template("login.html", error="Please log in first")

    user = User.query.get(user_id)
    if not user:
        return render_template("login.html", error="User not found")

    # You can pass data directly to template if you want username to appear there
    return render_template("profile.html", username=user.username)


# 👤 Profile Data API (used by JS to show dynamic info)
@user_bp.route("/api/profile", methods=["GET"])
def api_profile():
    user_id = session.get("user_id")
    if not user_id:
        return jsonify({"error": "Not logged in"}), 401

    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    listings = Listing.query.filter_by(user_id=user.id).all()
    rentals = []  # Add later when rental system exists

    return jsonify({
        "user": {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "phone": user.phone,
            "role": user.role,
        },
        "listings": [l.to_dict() for l in listings],
        "rentals": rentals,
    })


# 👥 Debug Route – All Users
@user_bp.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify([
        {"id": u.id, "username": u.username, "email": u.email}
        for u in users
    ])
