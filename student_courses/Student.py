from student_courses import Course

class Student:
    def __init__(self, name: str, student_id: str):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course: Course):
        if course in self.courses:
            print("You have already enrolled to this course")
        else:
            self.courses.append(course)

    def drop(self, course: Course):
        if course not in self.courses:
            print("You didn't enroll to this course")
        else:
            self.courses.remove(course)

    def view_courses(self):
        print(f"Courses for {self.name} ({self.student_id}):")
        for course in self.courses:
            print(f"  - {course}")

    def __str__(self):
        return f"{self.name} ({self.student_id})"

    def __eq__(self, other):
        return self.name == other.name and self.student_id == other.student_id
