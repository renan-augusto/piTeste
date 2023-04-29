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
    
class students(db.Model):
    __tablename__= "students"
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    student_academic_id = db.Column(db.String(30), nullable = False)

    def __repr__(self):
        return '<name %r>' % self.name