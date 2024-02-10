class Bank:
    name = "XY Bank"

    def __init__(self, balance):
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount > 0:
            if amount > self.balance:
                print("your account don't have this much money")
            elif amount < self.min_withdraw:
                print(f"fokira, you cannot withdraw less then {self.min_withdraw}")
            elif amount > self.max_withdraw:
                print(f"bank will be fokir, max withdraw limit is {self.max_withdraw}")
            else:
                self.balance - +amount
                print(f"here is your money {amount}")
                print(f"your current balance is sel {self.balance}")


my_account = Bank(5000)
print(my_account.balance)
my_account.deposit(1000)
print(my_account.balance)
my_account.withdraw(50000)
my_account.withdraw(100)
