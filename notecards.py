""" A rudimentary notecard app """

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    """ home page """
    return render_template('home.html', message="Fuck off my homepage template world!")
