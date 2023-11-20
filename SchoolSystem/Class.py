class SchoolClass:
    def __init__(self, class_id, name, designated_time, subject, classroom):
        self.class_id = class_id
        self.name = name
        self.designated_time = designated_time
        self.subject = subject
        self.student_group = None
        self.teacher = None
        self.classroom = classroom

    def enroll_group(self, group):
        self.student_group = group

    def assign_teacher(self, teacher):
        if self.teacher:
            print(f"Error: {self.name} already has a teacher.")
        else:
            self.teacher = teacher
            teacher.classes_taught.append(self)
    def __str__(self):
        return f"School Class {self.name} (ID: {self.class_id}) at {self.designated_time}."

