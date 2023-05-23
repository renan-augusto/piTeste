from spe import app, db
from flask import render_template, url_for, request, session, flash, redirect
from helpers import StudentForm
from models import Students, Internships

@app.route('/attendance')
def attendance():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('attendance')))
    internships_list = Internships.query.order_by(Internships.internshipsName)
    return render_template('attendance.html', internships=internships_list)

@app.route('/students-table')
def students():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('students')))
    students_list = Students.query.order_by(Students.studentName)
    return render_template('students.html', students=students_list)
    
@app.route('/registration')
def registration():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('create')))
    form = StudentForm()
    return render_template('register-student.html', form=form)

@app.route('/create-student', methods=['POST',  ])
def create():
    form = StudentForm(request.form)
    if not form.validate_on_submit():
        return redirect(url_for('create'))

    studentName = form.studentName.data
    studentEmail = form.studentEmail.data
    studentAcademicId = form.studentAcademicId.data
    studentDiscipline = form.studentDiscipline.data

    student = Students.query.filter_by(studentName=studentName).first()

    if student:
        flash('Aluno já cadastrado no sistema')
        return redirect(url_for('registration'))

    new_student = Students(studentName=studentName, studentEmail=studentEmail, studentAcademicId=studentAcademicId, studentDiscipline=studentDiscipline)
    db.session.add(new_student)
    db.session.commit()

    return redirect(url_for('students'))

