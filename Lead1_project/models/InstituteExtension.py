from db import db


class InstituteExtensionModel(db.Model):
    __tablename__ = "InstituteExtension"

    extensionId = db.Column(db.Integer, primary_key=True)
    fkInstituteId = db.Column(db.Integer, db.ForeignKey("fkInstituteId"), unique=False, nullable=False)
    extension = db.Column(db.String(100), unique=True, nullable = False)
    createdAt = db.Column(db.DateTime, unique = True, nullable = False)

    institute = db.relationship("InstituteModel", back_populates="InstituteExtension")
    

