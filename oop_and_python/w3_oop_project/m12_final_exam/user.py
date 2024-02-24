from transaction import Withdraw


class User:
    def __init__(self, name, email, password, is_admin, account_number) -> None:
        self.name = name
        self.email = email
        self.password = password
        self.is_admin = is_admin
        self.account_number = account_number


class AccountHolder(User):
    def __init__(
        self,
        name,
        email,
        password,
        account_type,
        account_number,
        is_admin=False,
        balance=0,
    ) -> None:
        self.__balance = balance
        self.account_type = account_type
        self.__transaction_list = []
        self.__loan_limit = 2
        super().__init__(name, email, password, is_admin, account_number)

    def deposit_money(self, money):
        if money > 0:
            self.__balance += money
            return True
        else:
            return False

    def withdraw_money(self, amount):
        transaction = Withdraw(amount, self.account_number)
        self.__transaction_list.append(transaction)
        if amount <= self.__balance:
            self.__balance -= amount
            transaction.success
            print(f"{amount} TK withdraw successfully \n")
        else:
            transaction.failed
            print("Withdrawal amount exceeded \n")

    @property
    def balance(self):
        return self.__balance

    # @balance.setter
    # def balance(self, amount):
    #     if amount > 0:
    #         self.__balance += amount

    def check_transaction_history(self):
        for transaction in self.__transaction_list:
            print(transaction)

    def transfer_money(self, amount):
        if amount > 0 and self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def __str__(self) -> str:
        return f"AC holder name: {self.name}, email: {self.email}, AC number: {self.account_number}, AC type: {self.account_type}"

    def add_transaction(self, transaction):
        if transaction:
            self.__transaction_list.append(transaction)

    @property
    def loan_limit(self):
        return self.__loan_limit

    @loan_limit.setter
    def loan_limit(self, a):
        if self.__loan_limit > 0:
            self.__loan_limit -= 1
            return True
        else:
            return False


class Admin(User):
    def __init__(self, name, email, password, account_number, is_admin=True) -> None:
        super().__init__(name, email, password, is_admin, account_number)

    def __str__(self) -> str:
        return f"Admin name: {self.name}, email: {self.email}, AC number: {self.account_number}, AC type: {self.account_type}"
