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

        start_date, start_time = str(lecture.start).split(" ")
        start_date = " ".join(start_date.split("-")[::-1])
        start_time = ":".join(start_time.split(":")[0:2])

        end_date, end_time = str(lecture.end).split(" ")
        end_date = " ".join(end_date.split("-")[::-1])
        end_time = ":".join(end_time.split(":")[0:2])

        res["lectures"].append({
            "id": str(lecture.id),
            "title": lecture.title,
            "description": lecture.description,
            "courseId": str(lecture.course_id),
            "start": start_date + " " + start_time,
            "end":  end_date + " " + end_time
        })

    for c in Course.select():
        res["courses"].append({
            "courseId": str(c.id),
            "coursename": c.title,
            "coursedescription": c.description
        })

    return str(res)


app.run()
