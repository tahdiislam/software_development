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
            if user_type == "seller":
                is_seller = None
                for seller in self.sellers:
                    if seller.email == email:
                        is_seller = seller
                if not is_seller:
                    print("email is invalid")
                elif is_seller.password != password:
                    print("password is invalid")
                elif is_seller.password == password:
                    print("seller login successfully")
                    return is_seller
            elif user_type == "customer":
                is_customer = None
                for customer in self.customers:
                    if customer.email == email:
                        is_customer = customer
                if not is_customer:
                    print("email is invalid")
                elif is_customer.password != password:
                    print("password is invalid")
                elif is_customer.password == password:
                    print("customer login successfully")
                    return is_customer
        else:
            print("email or password is missing")

    def create_product(self, name, price, quantity, seller_email):
        if name and price and quantity and seller_email:
            product = Product(name, price, quantity, seller_email)
            self.products.append(product)
            return True
        return False

    def see_all_product(self):
        for product in self.products:
            if product.quantity > 0:
                print(
                    f"name: {product.name}, price: {product.price}, available: {product.quantity}"
                )

    def buy_product(self, name, quantity, amount):
        if name and quantity and amount:
            is_product = None
            for product in self.products:
                if product.name == name:
                    is_product = product
            if not is_product:
                print("wrong product name entered")
            elif is_product.quantity >= quantity:
                total = is_product.price * quantity
                if amount >= total:
                    is_product.quantity -= quantity
                    print(f"here is you {quantity} {is_product.name}")
                    if amount > total:
                        print(f"and here is your {amount - total} tk extra money")
                elif amount < total:
                    print("not enough money")
            elif is_product.quantity == 0:
                print("sorry this product is not available")
            elif is_product.quantity < quantity:
                print(f"sorry only {is_product.quantity} items is available")


new_shopping = Shopping("zia shopping")

current_user = None
option = None
while True:
    if not current_user:
        if option != 3:
            print("1. signup as a customer")
            print("2. signup as a seller")
            print("3. login")
            print("4. exit")
            option = int(input("enter your option: "))
        if option == 4:
            break
        elif option == 1:
            email = input("enter your email: ")
            password = input("enter password: ")
            new_customer = new_shopping.create_customer(email, password)
            if new_customer:
                option = 3
            else:
                print("some issue is occurred. try again later")
        elif option == 2:
            email = input("enter your email: ")
            password = input("enter password: ")
            new_seller = new_shopping.create_seller(email, password)
            if new_seller:
                option = 3
            else:
                print("some issue is occurred. try again later")
        elif option == 3:
            print("1. login as customer")
            print("2. login as seller")
            print("3. back to main page")
            new_option = int(input("enter your option: "))
            email = input("enter your email: ")
            password = input("enter your password: ")
            if new_option == 1:
                current_user = new_shopping.login_user(email, password, "customer")
                option = None
            elif new_option == 2:
                current_user = new_shopping.login_user(email, password, "seller")
                option == None
            elif new_option == 3:
                current_user = None
                option = None
    elif current_user:
        if current_user.user_type == "seller":
            print("press 1 for add product: ")
            print("press 2 for back to the main page")
            new_option = int(input("enter your option: "))
            if new_option == 1:
                product_name = input("enter product name: ")
                product_price = int(input("enter product price: "))
                product_quantity = int(input("enter product quantity: "))
                new_shopping.create_product(
                    product_name, product_price, product_quantity, current_user.email
                )
            elif new_option == 2:
                option = None
                current_user = None
        elif current_user.user_type == "customer":
            print("press 1 to see all product")
            print("press 2 for buy product")
            print("press 3 for back to main page")
            new_option = int(input("enter your option: "))
            if new_option == 1:
                new_shopping.see_all_product()
            elif new_option == 2:
                product_name = input("enter product name: ")
                product_quantity = int(input("enter prodcut quantity: "))
                amount = int(input("enter total price: "))
                new_shopping.buy_product(product_name, product_quantity, amount)
            elif new_option == 3:
                option = None
                current_user = None
