from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # existing_user = User.query.filter_by(email=email).first()
        # if existing_user:
        #     flash('Email already registered!', 'warning')
        #     return redirect(url_for('main.register'))

        # hashed_password = generate_password_hash(password)
        # new_user = User(username=username, email=email, password=hashed_password)
        # db.session.add(new_user)
        # db.session.commit()

        flash('Account created successfully! You can log in now.', 'success')
        return redirect(url_for('main.register'))

    return render_template('index.html')

