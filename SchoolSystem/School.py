from datetime import datetime


class School:
    def __init__(self):
        self.student_groups = []
        self.teachers = []
        self.subjects = []
        self.school_classes = []
        self.classrooms = []


    def add_student_group(self, group):
        self.student_groups.append(group)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_class(self, school_class):
        self.school_classes.append(school_class)

    def add_classroom(self, classroom):
        self.classrooms.append(classroom)

    def assign_teacher_to_class(self, teacher, school_class):
        if teacher not in self.teachers:
            print("Error: Teacher is not recorded in the system.")
        else:
            school_class.assign_teacher(teacher)

    def enroll_group_to_class(self, group, school_class):
        if group not in self.student_groups:
            print("Error: Group is not recorded in the system.")
        else:
            school_class.enroll_group(group)
