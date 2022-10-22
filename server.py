from flask import Flask
from db import Course, Lecture

app = Flask("LMS")

@app.route('/courses')
def courses():
    lectures = []
    courses = []
    
    for l in Lecture.select():
        lecture = {
           "duration": l.duration,
           "id": str(l.id),
           "title": l.title,
           "description": l.description,
           "courseId": str(l.course_id)
        }
        date, time = str(l.date).split(" ")
        date = " ".join(date.split("-")[::-1])
        time = ":".join(time.split(":")[0:2])
        lecture["date"] = date + " " + time
        lectures.append(lecture)

    for c in Course.select():
        course = {
            "courseId": str(c.id),
            "coursename": c.title,
            "coursedescription": c.description
        }
        courses.append(course)
    
    res = {
        "lectures": lectures,
        "courses": courses
    }
    
    return str(res)


app.run()