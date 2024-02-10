import random


class Exam:
    name = "Mid Term"

    def __init__(self, examine):
        self.examine = examine
        print(f"Thank you {examine}, for attending the Mid-term")

    def get_marks(self):
        return random.randrange(50, 100)


my_exam = Exam("Me")
print(my_exam.get_marks())
