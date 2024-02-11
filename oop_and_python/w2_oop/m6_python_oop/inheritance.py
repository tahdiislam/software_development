# inheritance
# common inheritance
class Gadget:
    def __init__(self, brand, color, price) -> None:
        self.brand = brand
        self.color = color
        self.price = price
    def run(self):
        return f"running gadget"
class Phone(Gadget):
    def __init__(self, brand, color, price, camera, two_sim) -> None:
        self.camera = camera
        self.two_sim = two_sim
        super().__init__(brand, color, price)
class Laptop(Gadget):
    def __init__(self, brand, color, price, ram, processor) -> None:
        self.processor = processor
        self.ram = ram
        super().__init__(brand, color, price)
class Camera(Gadget):
    def __init__(self, brand, color, price, lense, camera) -> None:
        self.camera = camera
        self.lense = lense
        super().__init__(brand, color, price)

my_phone = Phone('samusung', 'black', 30000, '48mp', True)
print(my_phone.brand, my_phone.camera)