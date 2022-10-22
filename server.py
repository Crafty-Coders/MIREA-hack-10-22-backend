from multiprocessing.sharedctypes import Value
from flask import Flask, render_template
from db import Course, Lecture
from viewModels import CoursesIndex

app = Flask("LMS")

@app.route('/courses')
def courses():
   pass

@app.route('/adminTools')
def adminTools():
   lecturesList = []
   coursesList = []
   for l in Lecture.select():
      lecturesList += [l]
   for c in Course.select():
      coursesList += [c]
   coursesIndexes = CoursesIndex(len(coursesList))

   return render_template('adminTools.html', lecturesList=lecturesList, coursesList=coursesList, coursesIndexes=coursesIndexes)

app.run()