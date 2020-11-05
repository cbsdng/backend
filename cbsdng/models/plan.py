from freenit.db import db
from peewee import TextField, IntegerField

Model = db.Model


class Plan(Model):
    name = TextField()
    memory = IntegerField()
