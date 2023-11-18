from SchoolSystem.Class import SchoolClass
from SchoolSystem.Classroom import Classroom
from SchoolSystem.School import School
from SchoolSystem.Student import Student
from SchoolSystem.StudentGroup import StudentGroup
from SchoolSystem.Subject import Subject
from SchoolSystem.Teacher import Teacher


def main():
    school = School()

    math_subject = Subject(1, "Math")
    physics_subject = Subject(2, "Physics")
    school.add_subject(math_subject)
    school.add_subject(physics_subject)

    math_teacher = Teacher(1, "Ann Kravets", "2023-01-01")
    physics_teacher = Teacher(2, "Olena Shevchenko", "2023-01-15")
    school.add_teacher(math_teacher)
    school.add_teacher(physics_teacher)

    student_group = StudentGroup("11-B")
    student1 = Student(1, "Maria", "2023-09-01")
    student2 = Student(2, "Bogdan", "2023-09-01")
    student_group.add_student_to_group(student1)
    student_group.add_student_to_group(student2)
    school.add_student_group(student_group)

    classroom = Classroom(1, "101", 30)
    school_class = SchoolClass(1, "Math", "9:00 AM", math_subject, classroom)
    school.add_classroom(classroom)
    school.add_class(school_class)

    school.assign_teacher_to_class(math_teacher, school_class)

    school.enroll_group_to_class(student_group, school_class)

    math_teacher.assign_grade(student1, math_subject, 90)
    physics_teacher.assign_grade(student2, physics_subject, 95)

    for student in student_group.students:
        student.view_grades()


if __name__ == "__main__":
    main()