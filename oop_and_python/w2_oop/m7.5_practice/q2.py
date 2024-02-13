class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Cricketer(Person):
    def __init__(self, name, age, height, weight) -> None:
        super().__init__(name, age, height, weight)

    def __gt__(self, other):
        if self.age > other.age:
            return f"{self.name} is older than {other.name}"
        elif self.age < other.age:
            return f"{other.name} is older than {self.name}"
        else:
            return f"they are same age"


sakib = Cricketer("Sakib", 38, 68, 91)
musfiq = Cricketer("Rahim", 36, 68, 88)
kamal = Cricketer("Kamal", 39, 68, 94)
jack = Cricketer("Jack", 38, 68, 91)
kalam = Cricketer("Kalam", 37, 68, 95)

print(sakib > musfiq)
print(sakib < musfiq)
print(kalam < jack)
print(jack > sakib
)
