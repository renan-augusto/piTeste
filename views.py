from spe import app, db
from flask import render_template, url_for, request, session, flash, redirect
from helpers import StudentForm
from models import Students

@app.route('/students-table')
def students():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('students')))
    students_list = Students.query.order_by(Students.student_name)
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
    
    student_name = form.student_name.data
    student_email = form.student_email.data
    student_academic_id = form.student_academic_id.data
    
    student = Students.query.filter_by(student_name=student_name).first()
    
    if student:
        flash('Aluno já cadastrado no sistema')
        return redirect(url_for('registration'))
    
    new_student = Students(student_name=student_name, student_email=student_email, student_academic_id=student_academic_id)
    db.session.add(new_student)
    db.session.commit()
    
    return redirect(url_for('students'))