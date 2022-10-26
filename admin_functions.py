import datetime

from db import Course, Lecture


def addLecture(title="", description="", start="", end="", courseTitle=""):
    courseId = Course.select().where(Course.title == courseTitle)[0].id
    year, month, day, time = start.split(" ")
    h, m = time.split(":")
    start = datetime.datetime(year, month, day, h, m, 0, 0)
    year, month, day, time = end.split(" ")
    h, m = time.split(":")
    end = datetime.datetime(year, month, day, h, m, 0, 0)
    Lecture.insert(
        title=title,
        description=description,
        start=start,
        end=end,
        course=courseId
    ).execute()


def addCourse(title="", description=""):
    Course.insert(title=title, description=description).execute()
