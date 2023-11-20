from SchoolSystem.Class import SchoolClass
from SchoolSystem.Classroom import Classroom
from SchoolSystem.School import School
from SchoolSystem.Student import Student
from SchoolSystem.StudentGroup import StudentGroup
from SchoolSystem.Subject import Subject
from SchoolSystem.Teacher import Teacher


def main():
    school_system = School()

    teacher1 = Teacher(1, "Ann Shevchenko", "2022-01-01")
    teacher2 = Teacher(2, "Ivan Franko", "2022-02-01")
    school_system.add_teacher(teacher1)
    school_system.add_teacher(teacher2)

    math_subject = Subject(1, "Mathematics")
    english_subject = Subject(2, "English")
    school_system.add_subject(math_subject)
    school_system.add_subject(english_subject)

    group1 = StudentGroup("11-A")
    group2 = StudentGroup("11-B")
    school_system.add_student_group(group1)
    school_system.add_student_group(group2)

    student1 = Student(1, "Maria Kravets", "2022-09-01")
    student2 = Student(2, "Bohdan Koval", "2022-09-01")
    student3 = Student(3, "David Lovets", "2022-09-01")
    student4 = Student(4, "Bohdana Hapak", "2022-09-01")
    school_system.add_student_to_group(student1, group1)
    school_system.add_student_to_group(student2, group1)
    school_system.add_student_to_group(student3, group2)
    school_system.add_student_to_group(student4, group2)

    classroom1 = Classroom(1, "101", 30)
    classroom2 = Classroom(2, "102", 25)
    school_system.add_classroom(classroom1)
    school_system.add_classroom(classroom2)

    school_class1 = SchoolClass(1, "Math", "9:00 AM", math_subject, classroom1)
    school_class2 = SchoolClass(2, "English", "10:30 AM", english_subject, classroom2)
    school_system.add_class(school_class1)
    school_system.add_class(school_class2)

    school_system.assign_teacher_to_class(teacher1, school_class1)
    school_system.assign_teacher_to_class(teacher2, school_class2)
    school_system.enroll_group_to_class(group1, school_class1)
    school_system.enroll_group_to_class(group2, school_class2)

    print(school_system)

    school_system.view_school_attribute(school_system.student_groups)

    school_system.view_school_attribute(school_system.teachers)

    school_system.view_school_attribute(school_system.subjects)

    school_system.view_school_attribute(school_system.school_classes)

    school_system.view_school_attribute(school_system.classrooms)

    teacher1.assign_grade(student1, math_subject, "10")
    teacher1.assign_grade(student2, math_subject, "11")
    teacher2.assign_grade(student3, english_subject, "9")
    teacher2.assign_grade(student4, english_subject, "11")

    student1.view_grades()
    student2.view_grades()
    student3.view_grades()
    student4.view_grades()


if __name__ == "__main__":
    main()