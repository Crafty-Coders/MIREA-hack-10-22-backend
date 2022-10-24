class CoursesIndex:
    def __init__(self, length):
        self.coursesIndexes = [0 for _ in range(length)]
        self.showCourseDialog = False
        self.showCourseLectures = False
        self.showLecturesDialog = False

    def toJSON(self):
        return {
            "coursesIndexes": self.coursesIndexes,
            "showCourseDialog": self.showCourseDialog,
            "showCourseLectures": self.showCourseLectures,
            "showLecturesDialog": self.showLecturesDialog
        }

    def showLectures(self):
        self.showCourseLectures = not self.showCourseLectures
        print("aboba", self.showCourseLectures)

    def addCourse(self):
        self.showCourseDialog = not self.showCourseDialog

    def addLecture(self):
        self.showLecturesDialog = not self.showLecturesDialog

    def changeIndOfCourse(self, index):
        self.coursesIndexes[index] = not self.coursesIndexes[index]
