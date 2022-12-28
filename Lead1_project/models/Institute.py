from db import db


class InstituteModel(db.model):
    __tablename__ = "Institute"

    instituteId = db.Column(db.Integer, primary_key = True)
    instituteName = db.Column(db.String(80), unique=True, nullable=False)
    createdAt = db.Column(db.DateTime, unique=True, nullable=False)

    instituteExtension = db.relationship("InstituteExtensionModel",back_populates="institute", lazy="dynamic", cascade="all, delete")
    

    