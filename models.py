from app import db,app
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy



class patients(db.Model):
    __tablename__ = 'patients'
    patientsid = db.Column(db.Integer, primary_key=True)
    patientname = db.Column(db.String(45), nullable=False)
    patientsurname = db.Column(db.String(45), nullable=False)
    disease = db.Column(db.String(45), nullable=False)
    undercareof = db.Column(db.String(45), nullable=False)
    contact = db.Column(db.Integer, nullable=False)
    dateofadmit = db.Column(db.DateTime(), default=datetime.utcnow)
    address = db.Column(db.String(100), nullable=False)
    roomno = db.Column(db.Integer)
    bedno = db.Column(db.Integer)
    
    def serialize(self):
        return {
            'patientsid': self.patientsid,
            'patientname': self.patientname,
            'patientsurname': self.patientsurname,
            'disease': self.disease,
            'undercareof': self.undercareof,
            'contact': self.contact,
            'dateofadmit': self.dateofadmit,
            'address': self.address,
            'roomno': self.roomno,
            'bedno': self.bedno
        }

with app.app_context():   
    db.create_all()