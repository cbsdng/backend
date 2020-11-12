from freenit.schemas.base import BaseSchema
from marshmallow import fields


class WebSocketSchema(BaseSchema):
    status = fields.String(description='status', dump_only=True)
