from spe import db

class users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    user_type = db.Column(db.String(10))
    password = db.Column(db.String(100), nullable = False)

    def __repr__(self):
        return '<Name %r>' % self.name

class Students(db.Model):
    __tablename__= "students"
    student_name = db.Column(db.String(100), nullable = False)
    student_email = db.Column(db.String(100), nullable = False, unique = True)
    student_academic_id = db.Column(db.String(30), nullable = False)
    student_discipline = db.Column(db.String(30), nullable = False)
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)

    def __repr__(self):
        return '<name %r>' % self.student_name

class Internships(db.Model):
    __tablename__ = "internships"
    internshipsName = db.Column(db.String(100), nullable = False, unique = True)
    internshipsId = db.Column(db.Integer, primary_key = True, autoincrement = True)

    def __repr__(self):
        return '<name %r>' % self.internshipsName

class Attendance(db.Model):
    __tablename__ = "attendance"
    attendance_student_id = db.Column(db.Integer, db.ForeignKey("students.student_id"), nullable = False)
    attendance_internships_id = db.Column(db.Integer, db.ForeignKey("internships.internshipsId"), nullable = False)
    attendanceID = db.Column(db.Integer, primary_key = True, autoincrement = True)

    def __repr__(self):
        return f"<Attendance id={self.attendanceID}>"

