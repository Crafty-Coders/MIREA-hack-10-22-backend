from typing import Text
import uuid
from peewee import *
from configparser import ConfigParser

# Чтение данных для подключения БД из конфига
db_cfg = ConfigParser()
db_cfg.read("DB.cfg")

# Создание объекта БД
db = PostgresqlDatabase(
    host=db_cfg["DB"]["DB_HOST"],
    database=db_cfg["DB"]["DB_NAME"],
    user=db_cfg["DB"]["DB_USER"],
    password=db_cfg["DB"]["DB_PASSWORD"]
)


# Создание объекта курса
class Course(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = TextField()
    description = TextField()

    class Meta:
        database = db


# Создание объекта лекции
class Lecture(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    title = TextField()
    description = TextField()
    start = DateTimeField()
    end = DateTimeField()
    course = ForeignKeyField(Course, backref="courses")

    class Meta:
        database = db


class AdminLogin(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    login = TextField()
    password = TextField()

    class Meta:
        database = db


class AdminSession(Model):
    id = UUIDField(primary_key=True, default=uuid.uuid4)
    access_token = TextField()
    refresh_token = TextField()
    admin_id = ForeignKeyField(AdminLogin, backref="adminsessions")
    start_time = DateTimeField()

    class Meta:
        database = db


# Функция для создания таблиц бд (используется один раз)
def create_tables():
    db.create_tables([Course, Lecture])

# create_tables()
