class Shop:
    cart = [] # cart is an class attribute

    def __init__(self, buyer):
        self.buyer = buyer

    def add_to_cart(self, item):
        self.cart.append(item)


mehjabeen = Shop("mehjabeen")
mehjabeen.add_to_cart("shoe")
mehjabeen.add_to_cart("phone")
print(mehjabeen.cart)

nisho = Shop('nisho')
nisho.add_to_cart('pant')
nisho.add_to_cart('belt')
nisho.add_to_cart('cap')
print(nisho.cart)