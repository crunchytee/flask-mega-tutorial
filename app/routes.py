from app import app
from flask import render_template
from app.forms import LoginForm

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

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title="Sign In", form=form)