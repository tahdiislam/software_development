from abc import ABC, abstractmethod


class User:
    def __init__(self, name, phone, email, address) -> None:
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address


class Customer(User):
    def __init__(self, name, money, phone, email, address) -> None:
        self.money = money
        self.__order = None
        self.due_amount = 0
        super().__init__(name, phone, email, address)

    @property
    def order(self):
        return self.__order

    @order.setter
    def order(self, order):
        self.__order = order

    def place_order(self, order):
        self.order = order
        self.due_amount += order.bill
        print(f"{self.name} placed an order with bill {order.bill}")

    def eat_food(self, order):
        print(f"{self.name} eating food {order.items}")

    def pay_for_order(self, amount):
        pass

    def pay_tips(self, tips_amount):
        pass

    def write_review(self, review):
        pass


class Employee(User):
    def __init__(
        self, name, phone, email, address, salary, starting_date, department
    ) -> None:
        self.salary = salary
        self.starting_date = starting_date
        self.department = department
        self.due_salary = salary
        super().__init__(name, phone, email, address)

    def receive_salary(self):
        self.due_salary = 0


class Chef(Employee):
    def __init__(
        self,
        name,
        phone,
        email,
        address,
        salary,
        starting_date,
        department,
        cooking_item,
    ) -> None:
        self.cooking_item = cooking_item
        super().__init__(name, phone, email, address, salary, starting_date, department)


class Server(Employee):
    def __init__(
        self, name, phone, email, address, salary, starting_date, department
    ) -> None:
        self.earning_tips = 0
        super().__init__(name, phone, email, address, salary, starting_date, department)

    def take_order(self, order):
        pass

    def transfer_order(self, order):
        pass

    def server_food(self, order):
        pass

    def take_tips(self, amount):
        self.earning_tips += amount


class Manager(Employee):
    def __init__(
        self, name, phone, email, address, salary, starting_date, department
    ) -> None:
        super().__init__(name, phone, email, address, salary, starting_date, department)
