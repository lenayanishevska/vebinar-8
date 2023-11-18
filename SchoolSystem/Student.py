class Student:
    def __init__(self, student_id, name, enrollment_date):
        self.student_id = student_id
        self.name = name
        self.enrollment_date = enrollment_date
        self.grades = []

    def view_grades(self):
        if not self.grades:
            print(f"{self.name} has no grades.")
        else:
            print(f"Grades for {self.name}:")
            for grade in self.grades:
                print(f"Subject: {grade.subject.name}, Value: {grade.value}, "
                      f"Class: {grade.school_class.name}, Teacher: {grade.teacher.name}")
