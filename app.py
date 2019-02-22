from flask import Flask, request, flash, redirect, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, FloatField
from wtforms.validators import InputRequired, Optional, Email
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from forms import 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'ihaveasecret'

debug = DebugToolbarExtension(app)

connect_db(app)
# db.create_all()


@app.route('/')
def home_page():
    ''' Display home page and pets to client. '''

    pets = Pet.query.all()

    return render_template('/index.html', pets=pets)
