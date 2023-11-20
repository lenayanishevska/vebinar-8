from SchoolSystem.Grade import Grade


class Teacher:
    def __init__(self, teacher_id, name, hire_date):
        self.teacher_id = teacher_id
        self.name = name
        self.hire_date = hire_date
        self.classes_taught = []

    def assign_grade(self, student, subject, value):
        for school_class in self.classes_taught:
            if school_class.subject == subject and school_class.student_group.has_student(student):
                if any(grade.subject == subject and grade.school_class == school_class for grade in student.grades):
                    print(f"Error: {student.name} already has a grade for {subject.name} in {school_class.name}.")
                else:
                    grade = Grade(student, subject, value, school_class, self)
                    student.grades.append(grade)
                    return
        print(f"Error: {self.name} is not assigned to teach {subject.name} in any class.")

    def __str__(self):
        return f"Teacher {self.name} (ID: {self.teacher_id}) hired on {self.hire_date}."
