# global function
balance = 3000


def buy(item, price):
    global balance
    print("previous balance", balance)
    balance -= price
    print(f"{item} buy successful and your current balance is {balance}")


buy("shirt", 500)
