from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods = ['GET', 'POST'])
def sign_up():
    
    if request.method == 'POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('E-Mail muss mehr als 4 Zeichen besitzen!', category = 'error')

        elif len(firstname) < 2:
            flash('Vorname müssen mehr als 2 Buchstaben haben!', category = 'error')

        elif password1 != password2:
            flash('Passwörter stimmen nicht überein!', category = 'error')

        elif len(password1) < 7:
            flash('Passwort muss mindestens 7 Zeichen besitzen!', category = 'error')

        else:
            flash('Erfolgreich angelegt', category = 'success')
            #add User to Database


    return render_template("sign_up.html")