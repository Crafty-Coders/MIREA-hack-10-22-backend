from multiprocessing.sharedctypes import Value
from flask import Flask, render_template
from db import Course, Lecture

app = Flask("LMS")

@app.route('/courses')
def courses():
   pass

@app.route('/adminTools')
def adminTools():
   lectures = []
   courses = []
   for l in Lecture.select():
      lectures += [l]
   for c in Course.select():
      courses += [c]
   return render_template('adminTools.html', lectures=lectures, courses=courses)
app.run()