class Shopping:
    def __init__(self, name):
        self.name = name
        self.cart = []

    def add_to_cart(self, item, price, quantity):
        product = {"item": item, "price": price, "quantity": quantity}
        self.cart.append(product)
        print(f"your updated card: {self.cart}")

    def remove_to_cart(self, item):
        new_cart = list(filter(lambda i: i["item"] != item, self.cart))
        self.cart = new_cart
        print(f"your updated card: {self.cart}")

    def checkout(self, amount):
        total = 0
        for item in self.cart:
            total += item["price"] * item["quantity"]
        print(f"total price is {total}")
        if amount < total:
            print(f"you need to give me {total - amount}")
        elif amount > total:
            print("here is your product")
            print(f"here is your change: {amount - total}")
        else:
            print("here is your product")


my_shopping = Shopping("me")
my_shopping.add_to_cart("alu", 50, 5)
my_shopping.add_to_cart("begun", 100, 2)
my_shopping.add_to_cart("shosha", 60, 3)
my_shopping.add_to_cart("gazor", 70, 1)

my_shopping.remove_to_cart("alu")
my_shopping.checkout(400)
