from flask import Flask, render_template, request, flash, redirect, session, jsonify
from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = 'yliwmhd'
app.jinja_env.undefined = StrictUndefined

@app.route("/clock")
def home():
    return render_template("clock.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)