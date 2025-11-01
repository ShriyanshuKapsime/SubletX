from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app import db
from app.models.user import User

main = Blueprint('main', __name__)

@main.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if not name or not email or not password:
            flash('Please fill out all fields.', 'warning')
            return redirect(url_for('main.register'))

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'warning')
            return redirect(url_for('main.register'))

        # create user with only accepted constructor args
        new_user = User(name=name, email=email)

        # use the model's helper to set password (recommended)
        new_user.set_password(password)
        # alternatively: new_user.password_hash = generate_password_hash(password)

        db.session.add(new_user)
        db.session.commit()

        flash('Account created successfully! You can log in now.', 'success')
        return redirect(url_for('main.guest'))

    return render_template('register.html')

