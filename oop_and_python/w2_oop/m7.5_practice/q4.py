# write what are getter and setter in python with proper example.
""" 
the purpose of using getter and setter in object-oriented program to ensure data encapsulation.
private variable are not actually hidden in python. we can use getter and setter method to add validation login around getting and setting value. to avoid direct access of a class field i.e. private variable cannot be accessed or modified by external user.
"""
from q2 import Person


class Employee:
    def __init__(self, name, age, height, weight, salary) -> None:
        self.__salary = salary
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, s):
        if s > 0:
            self.__salary = s
        else:
            raise ValueError("provide a valid value")


employee_01 = Employee("01", 33, 66, 77, 20000)
employee_01.salary = 55000
print(employee_01.salary)
