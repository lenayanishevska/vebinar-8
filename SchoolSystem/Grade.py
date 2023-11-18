class Grade:
    def __init__(self, student, subject, value, school_class, teacher):
        self.student = student
        self.subject = subject
        self.value = value
        self.school_class = school_class
        self.teacher = teacher

    def __str__(self):
        return f"Grade {self.value} given by {self.teacher.name} for {self.subject.name} in {self.school_class.name} to {self.student.name}."

