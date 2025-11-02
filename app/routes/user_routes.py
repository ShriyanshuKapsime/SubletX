from flask import Blueprint, jsonify, render_template
from app.models.user import User

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{"id": u.id, "username": u.username, "email": u.email} for u in users])
    #return render_template("index.html")
@user_bp.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@user_bp.route("/browse", methods=['GET'])
def browse():
    return render_template("browse.html")

@user_bp.route("/listing", methods=['GET'])
def listing():
    return render_template("listing.html")

@user_bp.route('/profile', methods=['GET'])
def profile():
    return render_template("profile.html")