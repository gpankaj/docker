from flask_wtf import Form

from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField, SelectMultipleField, TextAreaField,validators, HiddenField
from wtforms.validators import Required, Length, Email, EqualTo

class LoginInfoForm(Form):
    hostname = StringField('HostName', [Required()])
    password  = PasswordField('Unix Password')
    label = StringField('Label')
    save = BooleanField('Save')
    submit = SubmitField('Submit')