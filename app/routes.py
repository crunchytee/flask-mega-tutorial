from werkzeug.utils import redirect
from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm
from app.models import User
from flask_login import login_user, current_user


@app.route("/")
@app.route("/index")
def index():
    user = {"username": "tosh"}
    posts = [
        {
            "author": {"username": "squash"},
            "body": "A rainy day in Portland!"
        },
        {
            "author": {"username": "Susan"},
            "body": "I'm tired from driving all day!"
        }
    ]
    return render_template("index.html", title="Home", user=user, posts=posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("index"))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash("invalid username or password")
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template("login.html", title="Sign In", form=form)
