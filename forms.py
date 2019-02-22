from flask_wtf import FlaskForm
from flask_debugtoolbar import DebugToolbarExtension
from models import Pet, db, connect_db
from wtforms.validators import InputRequired, Optional
from wtforms import StringField, IntegerField, BooleanField, TextAreaField


class AddPet(FlaskForm):
    ''' Form for adding pets '''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = StringField('Species', validators=[InputRequired()])
    photo_url = StringField('Photo URL')
    age = IntegerField('Age', validators=[InputRequired()])
    notes = TextAreaField('Notes')

