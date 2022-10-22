class CoursesIndex:
    def __init__(self, length):
        self.coursesIndexes = [0 for i in range(length)]
        self.showCourseDialog = False
        self.showCourseLectures = False
        self.showLecturesFields = False
    def showLectures(self):
        self.showCourseLectures = not self.showCourseLectures

    def addCourse(self):
        self.showCourseDialog = not self.showCourseDialog 

    def addLecture(self):
        self.showLecturesFields = not self.showLecturesFields

    def changeIndOfCourse(self, index):
        self.coursesIndexes[index] = not self.coursesIndexes[index]
