import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, SelectField

class UserForm(FlaskForm):
    email = StringField('Email', [validators.DataRequired(), validators.Length(min=3, max=100)] )
    password = PasswordField('Password', [validators.DataRequired(), validators.Length(min=8, max=100)])
    login = SubmitField('Login')

class StudentForm(FlaskForm):
    studentName = StringField('Nome do estudante', [validators.DataRequired(), validators.Length(min=1, max=100)])
    studentEmail = StringField('Email', [validators.DataRequired(), validators.Length(min=1, max=100)])
    studentAcademicId = StringField('RA', [validators.DataRequired(), validators.Length(min=1, max=30)])
    internship = SelectField('Estágio', [validators.DataRequired()], coerce=int)
    save = SubmitField('Salvar')
    