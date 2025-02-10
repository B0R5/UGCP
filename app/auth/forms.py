from flask import render_template, redirect, url_for, flash
from flask_login import login_user
from app import db
from app.database.models import User
from app.auth.forms import RegistrationForm

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)  # Haszowanie hasła
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        login_user(user)  # Logowanie użytkownika po rejestracji
        return redirect(url_for('dashboard'))  # Zmienić na odpowiednią stronę po rejestracji
    return render_template("register.html", form=form)
