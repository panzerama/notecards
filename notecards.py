""" A rudimentary notecard app """

from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField


class NewCardForm(FlaskForm):
    front = StringField('front')

app = Flask(__name__)

notecards = {"Donald": "Lee",
             "Stephen": "Anderson",
             "Dale": "Thomas",
             "Christopher": "Berger",
             "Savannah": "David",
             "Christopher": "Gardner",
             "Kathryn": "Martin",
             "Shelley": "Holden",
             "Amy": "Ramirez",
             "Carolyn": "Roberts",
             "Michael": "Hall",
             "Melissa": "Gray",
             "Michelle": "Vincent",
             "Mark": "Brown",
             "Zachary": "Morris",
             "Curtis": "Jenkins"}

app.secret_key = b'lij8iujfase232./a/sdafi234'

@app.route("/", methods=['GET'])
def home():
    """ home page """
    form = NewCardForm()
    return render_template('home.html',
                           message="Fuck off my homepage template world!",
                           form=form,
                           notecards=notecards)


@app.route("/new", methods=['POST'])
def new_card():
    """creates a new card"""
    return render_template('new_card.html', front=request.form['front'], back="a thing")
