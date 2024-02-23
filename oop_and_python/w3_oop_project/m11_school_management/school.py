class School:
    def __init__(self, name, address) -> None:
        self.name = name
        self.address = address
        self.teachers = {}
        # composition
        self.classrooms = {}

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        className = student.classRoom.name
        if className in self.classrooms:
            # TODO: set student id, (roll number) at the time of adding the student
            self.classrooms[className].add_student(student)
        else:
            print(f"No, classroom as named {className}")


class ClassRoom:
    def __init__(self, name) -> None:
        self.name = name
        # composition
        self.students = []

    def add_student(self, student):
        serial_id = f"{self.name}-{len(self.students) + 1}"
        student.id = serial_id
        self.students.append(student)

    def __str__(self) -> str:
        return f"{self.name}-{len(self.students)}"

    # TODO: sort student by grade
    def get_top_students(self):
        pass
