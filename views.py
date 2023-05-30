from spe import app, db
from flask import render_template, url_for, request, session, flash, redirect
from helpers import StudentForm, RegisterAttendanceForm
from models import Students, Internships, Attendance
from datetime import datetime

@app.route('/attendance')
def attendance():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('attendance')))
    internships_list = Internships.query.order_by(Internships.internshipsName)
    return render_template('attendance.html', internships=internships_list)

@app.route('/attendance/<int:internshipsId>')
def studentInternship(internshipsId):
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('attendance')))
    form = RegisterAttendanceForm()
    students_list = Students.query.filter_by(internship_id=internshipsId).all()
    student_choices = [(student.studentId, student.studentName) for student in students_list]
    form.selected_students.choices = student_choices
    internship = Internships.query.get_or_404(internshipsId)
    return render_template('filtered-students.html', internship=internship,form=form)

@app.route('/register-attendance', methods=['POST', ])
def registerAttendance():
    form = RegisterAttendanceForm()
    internship_id = form.internship_id.data
    students = Students.query.filter_by(internship_id=internship_id).all()
    student_choices = [(student.studentId, student.studentName) for student in students]
    form.selected_students.choices = student_choices
    
    if form.validate_on_submit():
        current_date = datetime.now()
        selected_students = form.selected_students.data
        
        for student_id in selected_students:
            new_attendance = Attendance(attendance_student_id=student_id, attendanceDate=current_date)
            db.session.add(new_attendance)
        
        db.session.commit()
        flash('Presenças registradas com sucesso!')
        return redirect(url_for('attendance', form=form))
    
    flash('Não foi possível cadastrar a presença. Por favor, tente novamente mais tarde.')
    return redirect(url_for('attendance'))
  

@app.route('/students-table')
def students():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('students')))
    students_list = Students.query.join(Internships).order_by(Students.studentName)
    return render_template('students.html', students=students_list)
    
@app.route('/registration')
def registration():
    if 'loggedUser' not in session or session['loggedUser'] == None:
        return redirect(url_for('index', advance=url_for('create')))
    form = StudentForm()
    form.internship.choices = [(internship.internshipsId, internship.internshipsName) for internship in Internships.query.all()] 
    return render_template('register-student.html', form=form)

@app.route('/create-student', methods=['POST', ])
def create():
    form = StudentForm(request.form) 
    form.internship.choices = [(internship.internshipsId, internship.internshipsName) for internship in Internships.query.all()]    
    if not form.validate_on_submit():
        return redirect(url_for('create'))

    studentName = form.studentName.data
    studentEmail = form.studentEmail.data
    studentAcademicId = form.studentAcademicId.data
    studentInternshipsId = form.internship.data

    student = Students.query.filter_by(studentName=studentName).first()

    if student:
        flash('Aluno já cadastrado no sistema')
        return redirect(url_for('registration'))

    new_student = Students(studentName=studentName, studentEmail=studentEmail, studentAcademicId=studentAcademicId, internship_id=studentInternshipsId)
    db.session.add(new_student)
    db.session.commit()

    return redirect(url_for('students'))

