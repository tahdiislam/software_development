""" 
1. read only--> you can not set the value, value cannot be changed
2. getter --> get value of a property through a method. most to the time you will get the value of a
private attribute
2. setter --> set value of a property through a method. most of the time you will set a value of a private property
"""


class User:
    def __init__(self, name, age, money) -> None:
        self.name = name
        self._age = age
        self.__money = money

    @property
    def age(self):
        return self._age

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if 0 > value:
            print("please pass a proper value")
        else:
            self.__money += value


samsu = User("kopa", 21, 10000)
# samsu.age()
print(samsu.age)
print(samsu.money)
samsu.money = 5000
print(samsu.money)
