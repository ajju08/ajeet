import uuid
from flask import request
from flask_smorest import Blueprint, abort
from flask.views import MethodView

from schemas import InstituteSchema
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import InstituteModel

blp = Blueprint("Institute",__name__,description="Operations on institutes")

@blp.route("/institute")
class InstituteList(MethodView):
    @blp.response(200, InstituteSchema(many=True))
    def get(cls):
        return InstituteModel.query.all()
    
    @blp.arguments(InstituteSchema)
    @blp.response(201, InstituteSchema)
    def post(self, institute_data):
        institute = InstituteModel(**institute_data)
        try:
            db.session.add(institute)
            db.seesion.commit()
        except IntegrityError:
            abort(400, message="A institute with that name already exists.",)
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the institute.")
        
        return institute
    
    @blp.route("/institute/<string:institute_id>")
    class Institute(MethodView):
        @blp.response(200, InstituteSchema)
        def get(self, institute_id):
            institute = InstituteModel.query.get_or_404(institute_id)
            return institute
        
        def delete(self, institute_id):
            institute = InstituteModel.query.get_or_404(institute_id)
            db.session.delete(institute)
            db.session.commit()
            return {"message": "Institute deleted"}, 200
        