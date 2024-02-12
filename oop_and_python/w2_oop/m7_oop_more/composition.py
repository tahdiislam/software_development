class Engine:
    def __init__(self, hp) -> None:
        self.hp = hp
    def start(self):
        print('engine has started')


class Driver:
    def __init__(self, name, experience) -> None:
        self.name = name
        self.experience = experience

# car 'has a' engine
class Car:
    def __init__(self, brand, color, price, hp, driver_name, driver_experience) -> None:
        self.brand = brand
        self.color = color
        self.price = price
        self.engine = Engine(hp)
        self.driver = Driver(driver_name, driver_experience)

    def __repr__(self) -> str:
        return f"car brand is: {self.brand}"
    def start_engine(self):
        self.engine.start()