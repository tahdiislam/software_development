# student class model
class Student:
    def __init__(self, name, current_class, id):
        self.name = name
        self.current_class = current_class
        self.id = id

    def __repr__(self):
        return f"student name: {self.name}, class: {self.current_class}"


# teacher class model
class Teacher:
    def __init__(self, name, subject, id):
        self.name = name
        self.subject = subject
        self.id = id

    def __repr__(self):
        return f"teacher's name: {self.name}, subject: {self.subject}"


# school class model
class School:
    def __init__(self, name):
        self.name = name
        self.teachers = []
        self.student = []

    def add_teacher(self, name, subject):
        id = len(self.teachers) + 101
        new_teacher = Teacher(name, subject, id)
        self.teachers.append(new_teacher)

    def enroll(self, name, current_class, fee):
        if fee < 6500:
            return "not enough money"
        else:
            id = len(self.student) + 1
            new_student = Student(name, current_class, id)
            self.student.append(new_student)
            return f"{name} is enroll with id: {id}, extra money {fee - 6500}"

    def __repr__(self) -> str:
        print(f"Welcome to our {self.name} school")
        print("--------------OUR TEACHER'S------------")
        for teacher in self.teachers:
            print(teacher)
        print("--------------OUR STUDENT'S------------")
        for student in self.student:
            print(student)
        return "all done"


phitron = School("Phitron")
phitron.add_teacher("ali akbor", "OOP")
phitron.add_teacher("tom cruise", "Algorithm")
phitron.add_teacher("Decap", "DS")
phitron.add_teacher("aj", "DB")

phitron.enroll("aliya", 9, 5000)
phitron.enroll("rani", 9, 8000)
phitron.enroll("vaijaan", 9, 7000)
print(phitron)
