from marshmallow import Schema, fields


class FooSchema(Schema):
    id = fields.String(required=True, dump_only=True)
    description = fields.String(required=True)
