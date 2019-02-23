from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Optional, URL, NumberRange
from wtforms import StringField, IntegerField, BooleanField, TextAreaField, SelectField


class AddPet(FlaskForm):
    ''' Form for adding pets '''

    name = StringField('Pet Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[("cat", "Cat"), ("dog", "Dog"),
                          ("porcupine", "Porcupine")])
    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    age = IntegerField('Age', validators=[InputRequired(),
                       NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes')

class EditPet(FlaskForm):

    photo_url = StringField('Photo URL', validators=[URL(), Optional()])
    notes = TextAreaField('Notes')
    is_available = BooleanField('Is Available')