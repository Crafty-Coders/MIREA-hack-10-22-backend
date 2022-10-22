from flask import Flask
from db import Course, Lecture

app = Flask("LMS")


@app.route('/courses')
def courses():
    res = {
        "lectures": [],
        "courses": []
    }

    for l in Lecture.select():
        date, time = str(l.date).split(" ")
        date = " ".join(date.split("-")[::-1])
        time = ":".join(time.split(":")[0:2])

        res["lectures"].append({
            "duration": l.duration,
            "id": str(l.id),
            "title": l.title,
            "description": l.description,
            "courseId": str(l.course_id),
            "date": date + " " + time
        })

    for c in Course.select():
        res["courses"].append({
            "courseId": str(c.id),
            "coursename": c.title,
            "coursedescription": c.description
        })

    return str(res)


app.run()
