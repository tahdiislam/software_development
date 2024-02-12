# @classmethod --> can be access without creating instance
# @staticmethod --> access without creating instance and self is not accessible inside the
# static method
# static attribute (class attribute)


class Shopping:
    cart = []  # class attribute or static attribute
    origin = "china"

    def __init__(self, name, location) -> None:
        self.name = name
        self.location = location

    def purchase(self, amount, price):
        remaining = amount - price
        print(
            f"you successfully purchase the product. here is your remaining money, {remaining}"
        )

    @staticmethod
    def multiply(*args):
        cnt = 1
        for n in args:
            cnt *= n
        print(cnt)

    @classmethod
    def hudai_dekhi(self, item):
        print(f"ac er howa khaite aschi, ar sateh {item} o dekhi, pocondho hoile nimu")


my_shopping = Shopping("jamu", "traffic jam area")
my_shopping.purchase(1000, 500)
# my_shopping.hudai_dekhi("lungi")
Shopping.hudai_dekhi("lungi")
Shopping.multiply(5, 5, 5)
