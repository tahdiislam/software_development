# 4 difference between classmethod and staticmethod
""" 
1. class method take cls as the first parameter, but the static method don't need any specific method
2. a class method can access or modify the class state. but a static method can't access or modify it
3. in general state method know nothing about the class method. they are utility type method that take 
    some parameter and work upon those parameter. on the other hand class method must have class a parameter
4. we use @classmethod decorator to create a class method on the other hand we use @staticmethod decorator to create a static method
"""
# example
from q1 import Person


class Cricketer(Person):
    def __init__(self, name, age, height, weight, exercise) -> None:
        self.exercise = exercise
        super().__init__(name, age, height, weight)

    @classmethod
    def play(self, method):
        print(f"sakib is {method}")

    @staticmethod
    def run(m):
        print(f"running {m} meter")


sakib = Cricketer("sakib", 38, 68, 80, True)
sakib.play("bolling")
sakib.run(30)
