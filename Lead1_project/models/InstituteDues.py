from db import db


class InstituteDuesModel(db.Model):
    __tablename__ = "InstituteDues"

    fkInstituteId = db.Column(db.Integer, primary_key = True)
    year = db.Column(db.Date, primary_key = True)
    status = db.Column()