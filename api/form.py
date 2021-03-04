from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    country = StringField('country', validators=[DataRequired()])
    submit = SubmitField('Submit')
