from University import University
from Course import Course
from Student import Student

uni = University("Harvard")

maths = Course("Mathematics", "MATH101")
physics = Course("Physics", "PHYS101")

uni.add_course(maths)
uni.add_course(physics)


alice = Student("Alice", "S101")

uni.add_student(alice)

alice.enroll(maths)

alice.view_courses()  # Output: Mathematics

uni.view_students()  # Output: Alice
uni.view_courses()