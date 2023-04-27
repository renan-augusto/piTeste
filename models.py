from spe import db

class users(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.integer, primary_key = True, autoincrement = True)
    name = db.Column(db.String(100), nullable = False)
    email = db.Column(db.String(100), unique = True, nullable = False)
    user_type = db.Column(db.String(10))
    password = db.Column(db.String(100))
    
    def __repr__(self):
        return '<Name %r>' % self.name