from flask_wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MyForm(Form):
    country = StringField('country', validators=[DataRequired()])
    submit = SubmitField('Submit')
