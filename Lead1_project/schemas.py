from marshmallow import Schema, fields


class PlainInstituteSchema(Schema):
    instituteId = fields.Int(dump_only=True)
    instituteName = fields.Str(required=True)
    createdAt = fields.DateTime(required=True)

class PlainInstituteExtensionSchema(Schema):
    extensionId = fields.Int(dump_only=True)
    fkInstituteId = fields.Int(required=True)
    extension = fields.Str(required=True)
    createdAt = fields.DateTime(required=True)

class InstituteExtensionUpdateSchema(Schema):
    fkInstituteId = fields.Int()
    extension = fields.Str()

class InstituteExtensionSchema(PlainInstituteExtensionSchema):
    Institute_id = fields.Int(required=True, load_only = True)
    institute = fields.Nested(PlainInstituteSchema(), dump_only=True)

class InstituteSchema(PlainInstituteSchema):
    institute = fields.List(fields.Nested(PlainInstituteExtensionSchema()),dump_only = True)





