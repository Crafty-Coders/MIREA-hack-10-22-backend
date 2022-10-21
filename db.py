from typing import Text
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
    title = TextField()
    description = TextField()
    
    class Meta:
        database = db
        

class Lecture(Model):
    title = TextField()
    description = TextField()
    date = DateTimeField()
    courseid = ForeignKeyField(Course, backref="lectures")

    class Meta:
        database = db
    
def createTables():
    db.create_tables([Course, Lecture])
    
# createTables()

