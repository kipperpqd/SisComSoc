from app.ext.db import db

class User(db.Model):
    
    __tablename__ = "users"
    
    id = db.Column("id", db.Integer, primary_key=True)
    email = db.Column("email", db.Unicode, unique=True, nullable=False)
    passwd = db.Column("passwd", db.Unicode)
    admin = db.Column("admin", db.Boolean)
    
    def __repr__(self):
        return '<User %r>' % self.email