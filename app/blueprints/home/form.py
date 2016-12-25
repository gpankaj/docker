__author__ = 'pankajg'

from flask_wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField, SelectMultipleField, TextAreaField,validators, HiddenField
from wtforms.validators import Required, Length, Email, EqualTo

class FilePath(Form):
    file_name_with_path = StringField('file_name')
    submit = SubmitField('Submit')