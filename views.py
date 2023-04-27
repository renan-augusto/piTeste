from spe import app
from flask import render_template, url_for, request, session, flash, redirect
from helpers import StudentForm
from flask_bcrypt import check_password_hash
# from models import users

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/auth', methods=['POST', ])
def auth():
    form = StudentForm(request.form)
    user = Users.query.filter_by(email = form.email.data).first()
    password = check_password_hash(user.password, form.password.data)
    if user and password:
        session['loggedUser'] = user.email
        flash(user.email + ' logado!')
        advance_page = request.form['advance']
        return redirect(advance_page)
    else:
        flash('Usuário ou senha incorretos - Não Logado')
    pass

@app.route('/create-student')
def create():
    return render_template('register-student.html')
    