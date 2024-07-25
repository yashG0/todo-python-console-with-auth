from db import dbConnect
from models.tweet import Todo
from models.user import User


dbConnect.connect()
dbConnect.create_tables([User])
dbConnect.create_tables([Todo])