import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class StudentForm(FlaskForm):
    name = StringField('Nome do estudante', [validators.DataRequired(), validators.Length(min=3, max=100)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)])
    ra = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=10)])
    