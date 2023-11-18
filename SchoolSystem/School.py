class School:
    def __init__(self):
        self.student_groups = []
        self.teachers = []
        self.subjects = []
        self.school_classes = []
        self.classrooms = []

    def add_student_group(self, group):
        if group not in self.student_groups:
            self.student_groups.append(group)
        else:
            print("Error: Group is already recorded in the system.")

    def add_student_to_group(self, student, group):
        if group in self.student_groups:
            if student not in group.students:
                group.students.append(student)
            else:
                print(f"Error: {student.name} is already enrolled in {group.group_id}.")
        else:
            print(f"Error: {group.group_id} is not enrolled in the school.")

    def add_teacher(self, teacher):
        if teacher not in self.teachers:
            self.teachers.append(teacher)
        else:
            print("Error: Teacher is already recorded in the system.")

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
        else:
            print("Error: Subject is already recorded in the system.")

    def add_class(self, school_class):
        if school_class not in self.school_classes:
            self.school_classes.append(school_class)
        else:
            print("Error: School class is already recorded in the system.")

    def add_classroom(self, school_classroom):
        if school_classroom not in self.classrooms:
            self.classrooms.append(school_classroom)
        else:
            print("Error: School classroom is already recorded in the system.")

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

    def expel_student(self, student):
        for group in self.student_groups:
            if student in group.students:
                group.students.remove(student)
                return
        print(f"Error: {student.name} is not enrolled in any student group.")

    def remove_group(self, group):
        if group in self.student_groups:
            self.student_groups.remove(group)
        else:
            print("Error: Group is not recorded in the system.")

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)
        else:
            print("Error: Teacher is not recorded in the system.")

    def remove_class(self, school_class):
        if school_class in self.school_classes:
            self.school_classes.remove(school_class)
        else:
            print("Error: School class is not recorded in the system.")

    def remove_classroom(self, classroom):
        if classroom in self.classrooms:
            self.classrooms.remove(classroom)
        else:
            print("Error: Classroom is not recorded in the system.")

    # зробити загальні два методи краще, ніж окремі для всього?
    def add_object(self, obj, obj_list):
        if obj not in obj_list:
            obj_list.append(obj)
        else:
            print(f"Error: {type(obj).__name__} is already recorded in the system.")

    def remove_object(self, obj, obj_list):
        if obj in obj_list:
            obj_list.remove(obj)
        else:
            print(f"Error: {type(obj).__name__} is not recorded in the system.")


    def view_school_attribute(self, list_to_view):
        for i in list_to_view:
            print(i)

    def __str__(self):
        return f"School with {len(self.student_groups)} student groups, {len(self.teachers)} teachers, " \
               f"{len(self.subjects)} subjects, {len(self.school_classes)} school classes, " \
               f"and {len(self.classrooms)} classrooms."
