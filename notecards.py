""" A rudimentary notecard app """

from flask import Flask, render_template, request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)


class CardForm(FlaskForm):
    front = StringField('front')
    back = TextAreaField('back')


class Notecard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    front = db.Column(db.String(400), unique=True, nullable=False)
    back = db.Column(db.String(400), unique=True, nullable=False)

    def __repr__(self):
        return '<Notecard %r>' % self.front

app.secret_key = b'lij8iujfase232./a/sdafi234'

@app.route('/', methods=['GET'])
def home():
    """ home page """
    form = CardForm()

    notecards = Notecard.query.all()

    return render_template('home.html',
                           message='All the notecards, all the time',
                           form=form,
                           notecards=notecards)


@app.route('/save', defaults={'card_id':None}, methods=['POST'])
@app.route('/save/<card_id>', methods=['POST'])
def save(card_id):
    """saves form value of card"""
    form = CardForm(request.form)

    if form.validate():
        if card_id:
            notecard = Notecard.query.get(card_id)
            form.populate_obj(notecard)

        else:
            new_notecard = Notecard()

            form.populate_obj(new_notecard)

            db.session.add(new_notecard)
    db.session.commit()

    notecards = Notecard.query.all()

    return redirect(url_for('home')) #render_template('home.html', message='New card added.', form=form, notecards=notecards)

@app.route('/review/<card_id>')
def review(card_id):
    notecard = Notecard.query.get(card_id)
    return render_template('review_card.html', notecard=notecard)

@app.route('/edit/<card_id>')
def edit(card_id):
    notecard = Notecard.query.get(card_id)
    form = CardForm()
    form.front.default = notecard.front
    form.back.default = notecard.back
    form.process()
    return render_template('edit_card.html', form=form, notecard_id=card_id)

@app.route('/delete/<card_id>')
def delete(card_id):
    notecard = Notecard.query.get(card_id)
    db.session.delete(notecard)
    db.session.commit()
    return redirect(url_for('home'))
