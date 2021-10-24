from flask import Blueprint, render_template, request, flash, redirect, url_for
from website import views
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash('Erfolgreich eingeloggt!', category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Falsches Passwort, erneut versuchen!', category='error')
        else:
            flash('E-Mail exisitiert leider nicht, bitte mit dieser E-Mail registrieren!', category='error')

    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("base.html")

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()

        if user:
            flash('Ein Account mit dieser E-Mail exisitiert bereits!', category='error')

        elif len(email) < 4:
            flash('E-Mail muss mehr als 4 Zeichen besitzen!', category = 'error')

        elif len(firstname) < 2:
            flash('Vorname müssen mehr als 2 Buchstaben haben!', category = 'error')

        elif password1 != password2:
            flash('Passwörter stimmen nicht überein!', category = 'error')

        elif len(password1) < 7:
            flash('Passwort muss mindestens 7 Zeichen besitzen!', category = 'error')

        else:
            new_user = User(email = email, firstname = firstname, password = generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Erfolgreich angelegt', category = 'success')
            return redirect(url_for('views.home'))



    return render_template("sign_up.html")