# inheritance provide "you a" relation

class Animal:
    def __init__(self, name) -> None:
        self.name = name

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class Tiger(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

class Person:
    def __init__(self, name) -> None:
        self.name = name

class Cricketer(Person):
    def __init__(self, name) -> None:
        super().__init__(name)