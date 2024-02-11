from abc import ABC, abstractmethod

# abstract base class


class Animal(ABC):
    @abstractmethod
    def eat(self):
        print("I love to eat")
    @abstractmethod
    def run(self, *args):
        cnt = 0
        for num in args:
            cnt+= num
        print(cnt)

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = name
        super().__init__()
    def eat(self):
        print('I love to eat banana')
    def run(self):
        return super().run(33, 334, 23, 3434)

layka = Monkey("lucky")
layka.eat()
layka.run()