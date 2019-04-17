from flask_wtf import Flaskform
from wtforms import StringField, PasswordField, BooleanField, SubmitField

class NavigationForm(FlaskForm):
	page = HiddenField('page')
	submit = SubmitField('next')
