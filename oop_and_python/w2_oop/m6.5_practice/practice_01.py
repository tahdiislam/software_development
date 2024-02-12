class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def __repr__(self) -> str:
        return f"product name: {self.name}, price: {self.price}"


class Shop:
    def __init__(self, name) -> None:
        self.__all_products = []
        self.name = name

    def add_product(self, name, price):
        prdc = Product(name, price)
        self.__all_products.append(prdc)

    def buy_product(self, item):
        prdc = next(
            (element for element in self.__all_products if element.name == item), None
        )
        print(prdc)
        if prdc != None:
            self.__all_products = list(
                filter(lambda x: x.name != item, self.__all_products)
            )
            print("congratulation you purchase the product")
        else:
            print("product is not available")

    def see_all_product(self):
        for prod in self.__all_products:
            print(prod)


my_shop = Shop("My Shop")
my_shop.add_product("alu", 50)
my_shop.see_all_product()
my_shop.buy_product("alu")
my_shop.add_product("begun", 50)
my_shop.see_all_product()