from flask import Blueprint, render_template, redirect, url_for
from forms import RegisterForm, LoginForm
from werkzeug.security import generate_password_hash

auth = Blueprint("auth", __name__)


@auth.route("/register", methods = ['GET', "POST"])
def register():
    forms = RegisterForm()

    if forms.validate_on_submit():
        username = forms.username.data
        password = forms.password.data
        harshed_password = generate_password_hash(password)

        return redirect(url_for("auth.login"))
    
    return render_template("register.html", form=forms)

@auth.route("/login", methods = ["GET", "POST"])
def login():
    forms = LoginForm()

    if forms.validate_on_submit():
        return "dashboard"

    return render_template("login.html", form = forms)