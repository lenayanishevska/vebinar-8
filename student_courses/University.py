from student_courses import Course, Student


class University:
    def __init__(self, _name):
        self._name = _name
        self.uni_courses = []
        self.students = []

    def add_course(self, course: Course):
        if course in self.uni_courses:
            print("This course is already added to the university")
        else:
            self.uni_courses.append(course)

    def add_student(self, student: Student):
        if student in self.students:
            print("This student is already added to the university")
        else:
            self.students.append(student)

    def view_courses(self):
        print(f"Courses in university ({self._name}):")
        for course in self.uni_courses:
            print(f"  - {course}")

    def view_students(self):
        print(f"Students in university ({self._name}):")
        for student in self.students:
            print(f"  - {student}")
