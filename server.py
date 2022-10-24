from multiprocessing.sharedctypes import Value
from flask import Flask, render_template, url_for, request
from db import Course, Lecture
from viewModels import CoursesIndex

app = Flask("LMS")


@app.route('/courses')
def courses():
    pass


@app.route('/adminTools', methods=["POST", "GET"])
def adminTools():
    
    lecturesList = []
    coursesList = []
    for l in Lecture.select():
        lecturesList += [l]
    for c in Course.select():
        coursesList += [c]
    courseParams = CoursesIndex(len(coursesList))
    if request.method == "POST":
        data = request.get_json()
        print(data)

        courseParams.showCourseLectures = data["showLectures"]
        courseParams.showCourseDialog = data["addCourse"]
        courseParams.showLecturesDialog = data["addLecture"]
    print(courseParams.toJSON())
    return render_template('adminTools.html', lecturesList=lecturesList, coursesList=coursesList, **courseParams.toJSON())


app.run()
