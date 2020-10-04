from app.ext.db import db

class Cad_cmt_om(db.Model):
            
    __tablename__ = "cad_cmt_om"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fullname = db.Column(db.String(80), unique=True, nullable=False)
    warname = db.Column(db.String(80), nullable=False)
    
        
    def __repr__(self):
        return '<Cmt OM %r>' % self.warname
    


class Person(db.Model):
            
    __tablename__ = "person"
    
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fullname = db.Column(db.String(80), unique=True, nullable=False)
    warname = db.Column(db.String(80), nullable=False)
    
        
    def __repr__(self):
        return '<Cmt OM %r>' % self.warname