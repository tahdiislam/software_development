# overloading and overriding


class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print("biriyani, polao, korma")


class Cricketer(Person):
    def __init__(self, name, age, height, weight, exercise, team) -> None:
        self.exercise = exercise
        self.team = team
        super().__init__(name, age, height, weight)

    def eat(self):  # overriding the parent eat method
        print("vegitables")

    def __mul__(self, other):
        return self.weight * other.weight

    def __gt__(self, other):
        return self.age > other.age
    def __len__(self):
        return self.height


sakib = Cricketer("sakib", 38, 68, 80, True, "BD")
# sakib.eat()

mushi = Cricketer("mushi", 37, 64, 75, True, "BD")

print(sakib * mushi)
print(sakib > mushi)
print(len(sakib))
