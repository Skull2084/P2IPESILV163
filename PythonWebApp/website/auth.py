from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db 
from flask_login import login_user, login_required, logout_user, current_user
from backend import verifier_affluence

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method=='POST':
        email=request.form.get('email')
        password=request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged In !', category="success")
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category="error")
        else:
            flash('No user with that email, please Sign In !', category="error")
    return render_template("login.html", user=current_user, affluence = verifier_affluence())

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign_up', methods=['GET', 'POST'])
def sign_up():
    if(request.method == 'POST'):
        email=request.form.get('email')
        password = request.form.get('password')
        user=User.query.filter_by(email=email).first()
        if user:
            flash('Account with this email already exists', category='error')
        elif "@edu.devinci.fr" not in email:
            flash('Not a Devinci Email', category="error")
            pass
        elif len(password)<4:
            flash('Password too short', category="error")
        else:
            flash('Account created', category="success")
            new_user=User(email=email, password=generate_password_hash(password, method='pbkdf2:sha256'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            return redirect(url_for('views.home'))
    return render_template("sign_up.html", user=current_user,affluence = verifier_affluence())

