class StudentGroup:
    def __init__(self, group_id):
        self.group_id = group_id
        self.students = []

    def add_student_to_group(self, student):
        self.students.append(student)

    def has_student(self, student):
        return student in self.students
