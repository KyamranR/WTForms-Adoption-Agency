from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, URL, AnyOf, Optional

class PetForm(FlaskForm):
    """Pets Form"""
    
    name = StringField('Name', validators=[InputRequired()])
    species = SelectField('Species', choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')], validators=[InputRequired(), AnyOf(['cat', 'dog', 'porcupine'], message='Invalid species')])
    photo_url = StringField('Photo URL', validators=[Optional(), URL()])
    age = IntegerField('Age', validators=[Optional()])
    notes = TextAreaField('Notes')
    available = BooleanField('Available')