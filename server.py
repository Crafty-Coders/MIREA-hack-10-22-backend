from flask import Flask
from db import Course, Lecture

app = Flask("LMS")


@app.route('/courses')
def courses():
    res = {
        "lectures": [],
        "courses": []
    }

    for lecture in Lecture.select():

        date, start_time = str(lecture.start).split(" ")
        date = ".".join(date.split("-")[::-1])
        start_time = ":".join(start_time.split(":")[0:2])

        _, end_time = str(lecture.end).split(" ")
        end_time = ":".join(end_time.split(":")[0:2])

        res["lectures"].append({
            "id": str(lecture.id),
            "title": lecture.title,
            "description": lecture.description,
            "courseId": str(lecture.course_id),
            "date": date,
            "start": start_time,
            "end":  end_time
        })

    for c in Course.select():
        res["courses"].append({
            "courseId": str(c.id),
            "coursename": c.title,
            "coursedescription": c.description
        })

    return str(res)


app.run()
