class User:
    def __init__(self, email, password, user_type) -> None:
        self.email = email
        self.password = password
        self.user_type = user_type


class Customer(User):
    def __init__(self, email, password, user_type, wallet) -> None:
        self.wallet = wallet
        super().__init__(email, password, user_type)


class Seller(User):
    def __init__(self, email, password, user_type) -> None:
        self.earning = 0
        super().__init__(email, password, user_type)

    def add_earning(self, amount):
        if amount:
            self.earning += amount
