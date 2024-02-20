from user import Customer, Seller
from product import Product


class Shopping:
    def __init__(self, name) -> None:
        self.name = name
        self.sellers = []
        self.customers = []
        self.products = []

    def create_seller(self, email, password):
        if email and password:
            seller = Seller(email, password, "seller")
            self.sellers.append(seller)
            return True
        return False

    def create_customer(self, email, password, initial_wallet=0):
        if email and password:
            customer = Customer(email, password, "customer", initial_wallet)
            self.customers.append(customer)
            return True
        return False
    def login_user(self, email, password, user_type):
        if email and password and user_type:
            if user_type == 'seller':
                

    def create_product(self, name, price, quantity, seller_email):
        if name and price and quantity and seller_email:
            product = Product(name, price, quantity, seller_email)
            self.products.append(product)
            return True
        return False
