# write difference between inheritance and composition with a proper example
""" 
***inheritance is a relation***
***composition has a relation***
"""
# inheritance
"""
Inheritance is a mechanism that allow us to inherit all the properties from the another class. The class
from which the properties and functionalities are utilized is called the parents class or super class
 or base class. The class which uses the property of the parents class called as child class or derived 
derived class. Inheritance is also called is a relation.
"""


# example
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __repr__(self) -> str:
        return f"the person name is {self.name}"


class Cricketer(
    Person
):  # this is called inheritance because it is a relation with the parent class
    def __init__(self, name, age, height, weight, exercise) -> None:
        self.exercise = exercise
        super().__init__(name, age, height, weight)


# composition
""" 
in composition a class that reference to one or more objects of other classes as an instance variable.
by using the class name or by creating the object we can access the member of one class inside another 
class. It enables creating complex types by combining different classes. It means that a class
composite can contain an object of another class component. this type of relation is known has a
relation
"""


# example
class Engine:
    def __init__(self, hp) -> None:
        self.hp = hp


class Driver:
    def __init__(self, name, experience) -> None:
        self.name = name
        self.experience = experience


class Car:
    def __init__(self, hp, driver_name, driver_experience, brand, color) -> None:
        self.engine = Engine(hp)
        self.driver = Driver(driver_name, driver_experience)
        self.color = color
        self.brand = brand

    def __repr__(self) -> str:
        return f"car brand is {self.brand}"
