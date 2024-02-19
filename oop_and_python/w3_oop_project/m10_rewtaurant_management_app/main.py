from menu import Burger, Drinks, Food, Menu, Pizza
from restaurant import Restaurant
from user import Chef, Manager, Customer, Server
from order import Order


def main():
    menu = Menu()
    # add pizzas
    pizza_1 = Pizza("Shutki Pizza", 600, "large", ["shutki", "onion"])
    pizza_2 = Pizza("Alu Vorta Pizza", 500, "large", ["potato", "onion"])
    pizza_3 = Pizza("Dar Pizza", 400, "large", ["dal", "onion"])
    menu.add_menu_item("pizza", pizza_1)
    menu.add_menu_item("pizza", pizza_2)
    menu.add_menu_item("pizza", pizza_3)

    # add burger
    burger_1 = Burger("Naga Burger", 1000, "chicken", ["bread", "chili"])
    burger_2 = Burger("Beef Burger", 1200, "beaf", ["goru", "haddi"])
    menu.add_menu_item("burger", burger_1)
    menu.add_menu_item("burger", burger_2)

    # add drinks
    mojo = Drinks("Mojo", 50, True)
    mocha = Drinks("Mocha Coffee", 300, False)
    menu.add_menu_item("drinks", mocha)
    menu.add_menu_item("drinks", mojo)

    # show menu
    menu.show_menu()

    # create restaurant
    restaurant = Restaurant("Sai Baba Restaurant", 2000, menu)

    # add employee
    manager = Manager(
        "kala chan", 34333, "kala@chan.com", "kaliapur", 1500, "jan 5 2023", "core"
    )
    restaurant.add_employee("manager", manager)
    chef = Chef(
        "Rustom Baburchi",
        343,
        "chupa@rustom.com",
        "rustam nagar",
        3500,
        "Dec 7 2023",
        "chef",
        ["pizza", "burger"],
    )
    restaurant.add_employee("chef", chef)
    server = Server(
        "chotu server", 443, "nai@jai.com", "restaurant", 200, "march 20 2023", "server"
    )
    restaurant.add_employee("server", server)
    restaurant.show_employee()

    # customer
    customer_02 = Customer("Sakib Khan", 100000, 3434, "sakib@khan.com", "banani")
    order_01 = Order(customer_02, [burger_1, mocha])
    customer_02.pay_for_order(order_01.bill)
    restaurant.add_order(order_01)

    # receive payment
    restaurant.receive_payment(order_01, 2000, customer_02)
    print(
        "restaurant revenue and balance after receive order 1 bill",
        restaurant.revenue,
        restaurant.balance,
    )

    customer_02 = Customer(
        "Sakib al hasan", 100000, 3434, "sakib@alhasan.com", "gulsan"
    )
    order_02 = Order(
        customer_02, [burger_1, mocha, burger_2, pizza_2, mojo, burger_1, burger_2]
    )
    customer_02.pay_for_order(order_02.bill)
    restaurant.add_order(order_02)

    # receive payment
    restaurant.receive_payment(order_02, 10000, customer_02)
    print(
        "restaurant revenue and balance after receive order 2 bill",
        restaurant.revenue,
        restaurant.balance,
    )

    # pay expense
    restaurant.pay_expense(1500, "tools")
    print(
        "restaurant revenue and balance and expense after paying some tool expense",
        restaurant.revenue,
        restaurant.balance,
        restaurant.expense,
    )
    restaurant.pay_salary(chef)
    print(
        "restaurant revenue and balance and expense after paying some chef salary",
        restaurant.revenue,
        restaurant.balance,
        restaurant.expense,
    )


if __name__ == "__main__":
    main()
