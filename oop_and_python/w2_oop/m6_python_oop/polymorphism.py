# poly -> many (multiple)
# morph -> shape
class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print("hamba hamba")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print('meow meow')
class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)
    def make_sound(self):
        print("gheu gheu")


my_cat = Cat("my_cat")
my_cat.make_sound()
my_dog = Dog('my_dog')
my_dog.make_sound()
