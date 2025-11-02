from flask import Blueprint, request, jsonify, session, redirect, url_for, render_template
from app.models.user import User
from app import db
import uuid

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

# === REGISTER ===
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')

    data = request.get_json(silent=True) or request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')
    phone = data.get('phone')
    role = data.get('role', 'user')

    if not all([username, email, password]):
        return jsonify({"error": "Username, email, and password required"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    user = User(id=str(uuid.uuid4()), username=username, email=email, phone=phone, role=role)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    session['user_id'] = user.id
    session['username'] = user.username

    # ✅ redirect to browse page instead of dashboard
    return jsonify({"message": "User registered successfully", "redirect": "/browse"}), 200


# === LOGIN ===
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    data = request.get_json(silent=True) or request.form
    email = data.get('email')
    password = data.get('password')

    if not all([email, password]):
        return jsonify({"error": "Email and password required"}), 400

    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    session['user_id'] = user.id
    session['username'] = user.username
    session['role'] = user.role

    # ✅ redirect to browse page instead of dashboard
    return jsonify({"message": "Login successful", "redirect": "/browse"}), 200


# === DASHBOARD === (you can keep for admins or future use)
@auth_bp.route('/dashboard', methods=['GET'])
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('auth_bp.login'))

    username = session.get('username')
    role = session.get('role')

    return render_template('dashboard.html', username=username, role=role)


# === LOGOUT ===
@auth_bp.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))
