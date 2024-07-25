from peewee import ForeignKeyField,CharField,BooleanField, Model
from config.db import dbConnect
from models.user import User


class Todo(Model):
    user = ForeignKeyField(User, backref="todos")
    title = CharField(max_length=30)
    desc = CharField(max_length=100)
    isCompleted = BooleanField(default=False)
    
    class Meta:
        database = dbConnect
        db_table = "todos"