from transaction import Transfer, Withdraw
from user import AccountHolder, Admin
from loan import Loan


class Bank:
    def __init__(self, name, address, initial_balance) -> None:
        self.name = name
        self.address = address
        self.__balance = initial_balance
        self.__all_customer_accounts = []
        self.__all_admin_accounts = []
        self.__transactions = []
        self.__all_loan = []
        self.__total_loan_amount = 0
        self.__bankrupt = False
        self.__loan_available = True
        self.__account_code = {"customer": "45222", "admin": "72333"}

    def add_customer_account(self, name, email, password, ac_type):
        ac_number = (
            f"{self.__account_code['customer']}-{len(self.__all_customer_accounts) +1}"
        )
        customer = AccountHolder(name, email, password, ac_type, ac_number)
        self.__all_customer_accounts.append(customer)
        return customer

    def add_admin_account(self, name, email, password):
        ac_number = (
            f"{self.__account_code['admin']}-{len(self.__all_admin_accounts) +1}"
        )
        admin = Admin(name, email, password, ac_number)
        self.__all_admin_accounts.append(admin)
        return admin

    def login_customer(self, email, password):
        if email and password:
            exist_user = None
            for user in self.__all_customer_accounts:
                if user.email == email:
                    exist_user = user
            if exist_user:
                if exist_user.password == password:
                    return exist_user
        return False

    def login_admin(self, email, password):
        if email and password:
            exist_admin = None
            for user in self.__all_admin_accounts:
                if user.email == email:
                    exist_admin = user
            if exist_admin:
                if exist_admin.password == password:
                    return exist_admin
        return False

    def delete_customer_account(self, email):
        self.__all_customer_accounts = list(
            filter(lambda user: user.email != email, self.__all_customer_accounts)
        )
        print("User deleted successfully \n")

    def show_all_customer_account(self):
        print("------------------- Account Holder---------------------")
        if len(self.__all_customer_accounts) == 0:
            print("No account found")
        for account in self.__all_customer_accounts:
            print(account)
        print("\n")

    @property
    def balance(self):
        return f"Available Balance: {self.__balance} \n"

    @balance.setter
    def balance(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount}TK balance added successfully")
        else:
            print("please provide a valid amount")

    @property
    def total_loan_amount(self):
        return f"Total loan provided: {self.__total_loan_amount} \n"

    def loan_available(self):
        if self.__loan_available:
            print("Loan is available \n")
        else:
            print("Loan is not available \n")

    def swap_loan_available(self):
        if self.__loan_available:
            self.__loan_available = False
            print("Loan feature is off \n")
        else:
            self.__loan_available = True
            print("Loan feature is on \n")

    def show_all_transaction(self):
        for transaction in self.__transactions:
            print(transaction)

    @property
    def bankrupt(self):
        return self.__bankrupt

    @bankrupt.setter
    def bankrupt(self, user):
        if user.is_admin:
            self.__bankrupt = True
            print("Bank is bankrupted \n")
        else:
            print("permission denied \n")

    def transfer_money(self, amount, sender, receiver_email):
        if (
            amount
            and sender
            and receiver_email
            and not self.__bankrupt
            and sender.balance >= amount
        ):
            receiver = None
            for user in self.__all_customer_accounts:
                if user.email == receiver_email:
                    receiver = user
            if receiver:
                new_transaction = Transfer(
                    amount, receiver.account_number, sender.account_number
                )
                self.__transactions.append(new_transaction)
                sender.add_transaction(new_transaction)
                receiver.add_transaction(new_transaction)
                decrease = sender.transfer_money(amount)
                increase = receiver.deposit_money(amount)
                if decrease and increase:
                    new_transaction.success
                    print(f"{amount} TK transfer successfully \n")
                else:
                    new_transaction.failed
                    print("Transaction is failed \n")
            else:
                print("Account does not exist \n")
        elif self.__bankrupt:
            print("Bank is bankrupt \n")
        elif sender.balance < amount:
            print("Transfer amount exceeded \n")

    def take_loan(self, amount, loan_taker):
        if (
            amount
            and loan_taker
            and not self.__bankrupt
            and self.__loan_available
            and loan_taker.loan_limit > 0
        ):
            new_loan = Loan(amount, loan_taker)
            if amount < self.__balance:
                self.__balance -= amount
                loan_taker.deposit_money(amount)
                loan_taker.loan_limit = 1
                new_loan.success
                self.__all_loan.append(new_loan)
                self.__total_loan_amount += amount
                print("Successfully take loan \n")
            else:
                new_loan.failed
                print("Loan amount exceeded \n")
        elif self.__bankrupt:
            print("Bank is bankrupted \n")
        elif not self.__loan_available:
            print("Currently loan is not available \n")
        elif loan_taker.loan_limit < 1:
            print("Your loan limit exceeded \n")
