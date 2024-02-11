from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    def __init__(self, name) -> None:
        self.name = name

    @abstractmethod
    def area(self, length, width):
        return length * width


class Square(Shape):
    def __init__(self, name) -> None:
        super().__init__(name)

    def area(self, length):
        print(length**2)


class Circle(Shape):
    def __init__(self, name) -> None:
        super().__init__(name)
    def area(self, radius):
        print(pi * radius**2)

my_square = Square("my_square")
my_square.area(5)

my_circle = Circle("my_circle")
my_circle.area(5)