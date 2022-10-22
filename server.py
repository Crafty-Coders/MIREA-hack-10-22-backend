from flask import Flask, render_template
from db import Course, Lecture

app = Flask("LMS")

@app.route('/courses')
def courses():
   pass

@app.route('/')
def homepage():
   return render_template('homepage.html')
app.run()