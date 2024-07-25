from peewee import CharField,Model
from config.db import dbConnect


class User(Model):
    username = CharField(unique=True, max_length=30)
    email = CharField(max_length=20)
    password = CharField(max_length=28)
    
    class Meta:
        database = dbConnect
        db_table = "users"