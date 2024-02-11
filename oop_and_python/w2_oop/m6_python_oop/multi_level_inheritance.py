# multi level inheritance
class Vehicle:
    def __init__(self, brand, color, price, driver) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.driver = driver
class Bus(Vehicle):
    def __init__(self, brand, color, price, driver, seat) -> None:
        self.seat = seat
        super().__init__(brand, color, price, driver)
class ACBus(Bus):
    def __init__(self, brand, color, price, driver, seat, ac) -> None:
        self.ac = ac
        super().__init__(brand, color, price, driver, seat)
my_bus = Bus('my line', 'blue', '5000000', 'me', 30)
print(my_bus.brand, my_bus.seat)
my_ac_bus = ACBus('My AC Line', 'green', 8000000, 'me', 45, True)
print(my_ac_bus.brand, my_ac_bus.color, my_ac_bus.driver, my_ac_bus.seat)