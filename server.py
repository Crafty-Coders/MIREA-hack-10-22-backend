from flask import Flask
from db import Course, Lecture

app = Flask("LMS")

@app.route('/courses')
def courses():
   pass


app.run()