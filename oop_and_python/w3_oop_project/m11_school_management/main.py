from school import ClassRoom, School
from person import Student, Teacher


def main():
    school = School("Adam zee", "uttora")
    eight = ClassRoom("eight")
    school.add_classroom(eight)
    nine = ClassRoom("nine")
    school.add_classroom(nine)
    ten = ClassRoom("ten")
    school.add_classroom(ten)

    abul = Student("abul", ten)
    school.student_admission(abul)


if __name__ == "__main__":
    main()
