import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators

class UserForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)] )
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=6, max=100)])
    save = SubmitField('Save')

class StudentForm(FlaskForm):
    name = StringField('Nome do estudante', [validators.DataRequired(), validators.Length(min=3, max=100)])
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)])
    ra = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=10)])
    