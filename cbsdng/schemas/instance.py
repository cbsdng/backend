import sys

from freenit.schemas.base import BaseSchema
from freenit.schemas.paging import PageOutSchema
from marshmallow import fields


class InstanceSchema(BaseSchema):
    id = fields.Number(dump_only=True)
    cpus = fields.Number(dump_only=True)
    curmem = fields.Number(dump_only=True)
    hostname = fields.String(dump_only=True)
    ip = fields.String()
    name = fields.String()
    ostype = fields.String(dump_only=True)
    path = fields.String(dump_only=True)
    pcpu = fields.Number(dump_only=True)
    ram = fields.Number(dump_only=True)
    state = fields.String(dump_only=True)
    type = fields.String(dump_only=True)
    vnc = fields.String(dump_only=True)


PageOutSchema(InstanceSchema, sys.modules[__name__])
