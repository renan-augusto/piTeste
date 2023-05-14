import mysql.connector
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Connecting...")

try:
    conn = mysql.connector.connect (
        host='127.0.0.1',
        user='root',
        password='admin'
    )
except mysql.connector.Error as err:
    if err.erno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('Existe algo errado no nome de usuario ou senha')
    else:
        print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `REGISTRO_ALUNOS_FAMERP`;")
cursor.execute("CREATE DATABASE `REGISTRO_ALUNOS_FAMERP`")
cursor.execute("USE `REGISTRO_ALUNOS_FAMERP`")

TABLES = {}
TABLES['users'] = ('''
      CREATE TABLE `users` (
      `user_id` int(11) NOT NULL AUTO_INCREMENT,
      `name` varchar(100) NOT NULL,
      `email` varchar(100) UNIQUE NOT NULL,
      `user_type` varchar(10) NOT NULL,
      `password` varchar(100) NOT NULL,
      PRIMARY KEY (`user_id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['students'] = ('''
      CREATE TABLE `students` (
      `student_id` int(11) NOT NULL AUTO_INCREMENT,
      `student_name` varchar(100) NOT NULL,
      `student_email` varchar(100) UNIQUE NOT NULL,
      `student_academic_id` varchar(30) NOT NULL,
      `student_discipline` varchar(30) NOT NULL, 
      PRIMARY KEY (`student_id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['internships'] = ('''
      CREATE TABLE `internships` (
      `internshipsId` int(11) NOT NULL AUTO_INCREMENT,
      `internshipsName` varchar(100) NOT NULL,
      PRIMARY KEY (`internshipsId`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

# INSERT INTO INTERNSHIP (internshipname) VALUES (%s);

TABLES['attendance'] = ('''
      CREATE TABLE `attendance` (
      `attendanceId` int(11) NOT NULL AUTO_INCREMENT,
      PRIMARY KEY (`attendance`),
      `attendance_student_id` INT NOT NULL,
      FOREIGN KEY (`student_id`) REFERENCES `students`(`student_id`) ON DELETE NO ACTION
      `attendance_internship_id` INT NOT NULL,
      FOREIGN KEY (`internship_id`) REFERENCES `internship`(`internshipid`) ON DELETE NO ACTION

      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for table_name in TABLES:
    table_sql = TABLES[table_name]
    try:
        print('Generating table {}:'.format(table_name), end=' ')
        cursor.execute(table_sql)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ABLE_EXISTS_ERROR:
            print('Already exists')
        else:
            print(err.msg)
    else:
        print('OK')

users_sql = 'INSERT INTO users (name, email, user_type, password) VALUES (%s, %s, %s, %s)'
users = [
    ("Renan Augusto", "renan@teste.com.br", "admin", generate_password_hash("projetointegrador").decode('utf-8')),
    ("Usuario Teste", "teste@teste.com.br", "admin", generate_password_hash("projetointegrador").decode('utf-8'))
]
cursor.executemany(users_sql, users)
cursor.execute('select * from REGISTRO_ALUNOS_FAMERP.users')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

students_sql = 'INSERT INTO students (student_name, student_email, student_academic_id, student_discipline) VALUES(%s, %s, %s, %s)'
students = [
    ("Wardell Stephen Curry II", "scurry@gsw.com", "GSW30", "Medicina"),
    ("Lebron Raymone James", "kingjames@lalakers.com", "0623LACL", "Medicina")
]
cursor.executemany(students_sql, students)
cursor.execute('select * from REGISTRO_ALUNOS_FAMERP.students')
print(' -------------  Estudantes:  -------------')
for student in cursor.fetchall():
    print(student[1])

conn.commit()

cursor.close()
conn.close()