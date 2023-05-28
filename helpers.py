import os
from spe import app
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, validators, SelectField, IntegerField, SelectMultipleField
from datetime import datetime
from spe import db
from models import Attendance

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
    
class FilterForm(FlaskForm):
    submit = SubmitField('Filtrar')
    
class RegisterAttendanceForm(FlaskForm):
    selected_students = SelectMultipleField('Alunos selecionados', coerce=int)
    internship_id = IntegerField('Id do estagio')
    submit = SubmitField('Registrar presença')

# def register_attendance(internship_id, selected_students):
#     current_date = datetime.now()
    
#     for student_id in selected_students:
#         attendance = Attendance(attendance_student_id=student_id, attendanceDate=current_date)
#         db.session.add(attendance)
#     db.session.commit()