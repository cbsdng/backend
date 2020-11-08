import sys
from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from marshmallow import fields


class PlanSchema(BaseSchema):
    id = fields.Integer(description='ID', dump_only=True)
    name = fields.String()
    memory = fields.Integer()


PageOutSchema(PlanSchema, sys.modules[__name__])
