# encapsulation --> hide details
# access modifier --> public, protected, private
class Bank:
    def __init__(self, holder_name, initial_balance) -> None:
        self.holder_name = holder_name
        self.__balance = initial_balance
        self._branch = "ramgonj"

    def deposit(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print("fokira")

    def check_balance(self):
        print(self.__balance)


my_account = Bank("Me", 50000)
my_account.deposit(5555)
my_account.check_balance()
print(my_account.holder_name, my_account._branch)
print(dir(my_account))
print(my_account._Bank__balance)
my_account._Bank__balance = 0
my_account.check_balance()
