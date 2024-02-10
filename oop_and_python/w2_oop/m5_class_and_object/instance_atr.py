class Shop:
    shoppingmall = "jamu"

    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []  # cart is an instance attribute

    def add_to_cart(self, item):
        self.cart.append(item)


mehjabeen = Shop("mehjabeen")
mehjabeen.add_to_cart("shoe")
mehjabeen.add_to_cart("drees")
mehjabeen.add_to_cart("mack-up items")
print(mehjabeen.cart)

nisho = Shop("nisho")

nisho.add_to_cart("cap")
nisho.add_to_cart("t-shirt")
nisho.add_to_cart("shirt")
nisho.add_to_cart("cap")
nisho.add_to_cart("belt")

print(nisho.cart)
