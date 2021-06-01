from flask import render_template
from app import app

@app.route("/")
@app.route("/index")
def index():
    user = {"username": "an"}
    posts = [
        {
            'author': {'username':'le'},
            'body' : 'Beautiful day'
        },
        {
            'author': {'username': 'le'},
            'body': 'The Avengers movie was so cool'
        }
    ]
    return render_template('index.html', title="Home", user = user, posts =posts)

