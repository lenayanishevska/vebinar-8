class StudentGroup:
    def __init__(self, group_id):
        self.group_id = group_id
        self.students = []

    def has_student(self, student):
        return student in self.students

    def __str__(self):
        return f"Student Group {self.group_id} with {len(self.students)} students."

