# what is inheritance? Explain with example

"""
inheritance means to inherit one class to another class. It provide reusability of code and prevent to 
duplicate code. the inherit class has access of all attribute of the parent or base class.
"""


class Vehicle:
    def __init__(self, brand, price, color) -> None:
        self.brand = brand
        self.price = price
        self.color = color

    def run(self):
        print("vehicle is running")


class Bus(Vehicle):
    def __init__(self, brand, price, color, seats) -> None:
        self.seats = seats
        super().__init__(brand, price, color)

    def __repr__(self) -> str:
        return f"Bus brand is: {self.brand}, price : {self.price}, color : {self.color}"


my_bus = Bus("green line", 5000000, "green", 50)
print(my_bus)
