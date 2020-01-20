from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'yliwmhd'
app.jinja_env.undefined = StrictUndefined

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/clock")
def clock():
    return render_template("clock.html")

@app.route("/forms")
def forms():
    return render_template("forms.html")

@app.route("/liftingstateup")
def liftingstateup():
    return render_template("liftingstateup.html")

@app.route("/lists")
def lists():
    return render_template("lists.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/mailbox")
def mailbox():
    return render_template("mailbox.html")

@app.route("/warning")
def warning():
    return render_template("warning.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)