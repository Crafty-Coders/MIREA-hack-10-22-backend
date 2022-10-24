from flask import Flask, render_template, request
from db import Course, Lecture

# создание flask-приложения
app = Flask("LMS")


@app.route('/courses')
def courses():
    res = {
        "lectures": [],
        "courses": []
    }  # Ответом на запрос является объекта, содержащий массивы лекций и курсов

    for lecture in Lecture.select():  # Перебираем лекции из БД

        # Дату начала разбиваем на дату и время
        date, start_time = str(lecture.start).split(" ")
        # Разбиваем дату на три числа, инвертируем и записываем через точку
        date = ".".join(date.split("-")[::-1])
        # Разбиваем время на три числа, отбрасываем секунды и записываем через :
        start_time = ":".join(start_time.split(":")[0:2])

        # Дату окончания разбиваем на дату и время, отбрасывая дату, так как она известна из времени начала
        _, end_time = str(lecture.end).split(" ")
        # Разбиваем время на три числа, отбрасываем секунды и записываем через :
        end_time = ":".join(end_time.split(":")[0:2])

        # Формируем словарь и добавляем его в массив лекций
        res["lectures"].append({
            "id": str(lecture.id),
            "title": lecture.title,
            "description": lecture.description,
            "courseId": str(lecture.course_id),
            "date": date,
            "start": start_time,
            "end": end_time
        })

    for c in Course.select():  # Перебираем курсы из БД
        #  Формируем словарь и добавляем его в массив курсов
        res["courses"].append({
            "courseId": str(c.id),
            "coursename": c.title,
            "coursedescription": c.description
        })

    # Возвращаем ответ на запрос
    return str(res)


@app.route("/adminLogin",  methods=['POST', 'GET'])
def admin_login():
    if request.method == 'POST':
        data = request.get_json()
        return "aboba"
    return render_template("adminlogin.html")


# Запуск flask-приложения
app.run()
