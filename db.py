from typing import Text
import uuid
from peewee import *
from configparser import ConfigParser

db_cfg = ConfigParser()
db_cfg.read("DB.cfg")

db = PostgresqlDatabase(
    host=db_cfg["DB"]["DB_HOST"],
    database=db_cfg["DB"]["DB_NAME"],
    user=db_cfg["DB"]["DB_USER"],
    password=db_cfg["DB"]["DB_PASSWORD"]
)


class Course(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = TextField()
    description = TextField()
    
    class Meta:
        database = db
        

class Lecture(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = TextField()
    description = TextField()
    date = DateTimeField()
    course = ForeignKeyField(Course, backref="courses")

    class Meta:
        database = db
    
def createTables():
    db.create_tables([Course, Lecture])
    
# createTables()
