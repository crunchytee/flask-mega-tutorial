from app import app
from flask import render_template

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