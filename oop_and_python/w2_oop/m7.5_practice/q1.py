# write what is meant by operator overloading and overriding with proper example.

# method overriding
""" 
in inheritance when a sub-class or child class has a same method which method is already exist in the 
parent or super class then the parent or super class method will be override by the child class and the 
child class method will be valid. it is called method overriding
"""


# example
class Animal:
    def __init__(self) -> None:
        pass

    def run(self):  # run method
        print("running")


class Dog(Animal):
    def __init__(self) -> None:
        super().__init__()

    def run(self):  # overriding the super class run method
        print("dog is running")


my_dog = Dog()
my_dog.run()  # dog is running

# operator overloading
""" 
in python we can change the way operator works for user defined types.
for example + operator perform arithmetic addition in two numbers, merge two lists and concat two 
strings. this features in python that allows the same operator to have different meaning according to 
the context called operator overloading. in class we defined what our operator will when we use an operator between our two different instance.
"""


# example
class Person:
    def __init__(self, name, age, height, weight) -> None:
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __repr__(self) -> str:
        return f"the person name is {self.name}, age: {self.age}, height: {self.height} and weight: {self.weight}."


class Player(Person):
    def __init__(self, name, age, height, weight, exercise) -> None:
        self.exercise = exercise
        super().__init__(name, age, height, weight)

    # we defined what will our + operator will do
    def __add__(self, other):
        return self.age + other.age  # this will add two player age and return it

    # this is checking two first player is other than the second player
    def __gt__(self, other):
        return self.age > other.age
    # when we use len in our instance then it will return the height of that instance
    def __len__(self):
        return self.height


sakib = Player("sakib", 38, 68, 80, True)
mushi = Player("mushi", 36, 64, 76, True)

print(sakib + mushi)  # we're using + operator between our two instance
# it will return the addition of two player age
print(
    sakib > mushi
)  # we have defined what will our greater than '>' operator will be do in your class method it will return which player is older
print(len(sakib)) # customize the len() function using operator overloading now this will return our player height