
class Course:
    def __init__(self, name, course_id):
        self.name = name
        self.course_id = course_id

    def __eq__(self, other):
        return self.name == other.name and self.course_id == other.course_id

    def __str__(self):
        return f"{self.name} ({self.course_id})"
