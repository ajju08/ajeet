import uuid
from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError
from schemas import InstituteExtensionSchema, InstituteExtensionUpdateSchema

from db import db
from models import InstituteExtensionModel

blp = Blueprint("InstituteExtension","InstituteExtension", description= "Operations on instituteExtension")


@blp.route("/instituteExtension/<string:extension_id")
class InstituteExtension(MethodView):
    @blp.response(200, InstituteExtensionSchema)
    def get(self, extension_id):
        extension = InstituteExtensionModel.query.get_or_404(extension_id)
        return extension
    
    def delete(self, extension_id):
        extension = InstituteExtensionModel.query.get_or_404(extension_id)
        db.session.delete(extension)
        db.session.commit()
        return {"message":"extension deleted."}
    
    @blp.arguments(InstituteExtensionUpdateSchema)
    @blp.response(200, InstituteExtensionSchema)
    def put(self, extension_data, extension_id):
        extension = InstituteExtensionModel.query.get(extension_id)
        if extension:
            extension.fkInstituteId = extension_data["fkInstituteId"]
            extension.extension = extension_data["extension"]
        else:
            extension = InstituteExtensionModel(extensionId=extension_id, **extension_data)

        db.session.add(extension)
        db.session.commit()

        return extension
    
@blp.route("/instituteExtension")
class InstituteExtensionList(MethodView):
    @blp.response(200, InstituteExtensionSchema(many=True))
    def get(self):
        return InstituteExtensionModel.query.all()
    
    @blp.arguments(InstituteExtensionSchema)
    @blp.response(201, InstituteExtensionSchema)
    def post(self, extension_data):
        extension = InstituteExtensionModel(**extension_data)

        try:
            db.session.add(extension)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the extension.")

        return extension
    