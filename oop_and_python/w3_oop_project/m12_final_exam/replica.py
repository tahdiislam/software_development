from bank import Bank

bank = Bank("Amar Bank", "amar alaka", 500000)

current_user = None

while True:
    if not current_user:
        print("Press 1 for create account")
        print("Press 2 for login")
        print("Press 3 for exit \n")
        option = int(input("Enter here: "))
        print("\n")
        if option == 1:
            print("Press 1 for create customer account")
            print("Press 2 for create admin account \n")
            two_option = int(input("Enter here: "))
            print("\n")
            if two_option == 1:
                print("Press 1 for Saving account")
                print("Press 2 for Current account \n")
                three_option = int(input("Enter here: "))
                print("\n")
                name = input("Enter your name: ")
                print("\n")
                email = input("Enter your email: ")
                print("\n")
                password = input("Enter password: ")
                print("\n")
                ac_type = None
                if three_option == 1:
                    ac_type = "saving"
                else:
                    ac_type = "current"
                customer = bank.add_customer_account(name, email, password, ac_type)
                if customer:
                    current_user = customer
                    print("Customer account created successfully \n")
                else:
                    print("Something is wrong, try again. \n")
            elif two_option == 2:
                name = input("Enter your name: ")
                print("\n")
                email = input("Enter your email: ")
                print("\n")
                password = input("Enter password: ")
                print("\n")
                admin = bank.add_admin_account(name, email, password)
                if admin:
                    current_user = admin
                    print("Admin account created successfully \n")
                else:
                    print("Something is wrong, try again \n")
        elif option == 2:
            print("Press 1 for customer login")
            print("Press 2 for admin login")
            print("\n")
            two_option = int(input("Enter here: "))
            print("\n")
            if two_option == 1:
                email = input("Enter your email: ")
                print("\n")
                password = input("Enter your password: ")
                print("\n")
                exist_user = bank.login_customer(email, password)
                if exist_user:
                    current_user = exist_user
                    print(f"Welcome {exist_user.name} \n")
                else:
                    print("Email or password is invalid \n")
            elif two_option == 2:
                email = input("Enter your email: ")
                print("\n")
                password = input("Enter your password: ")
                print("\n")
                exist_admin = bank.login_admin(email, password)
                if exist_admin:
                    current_user = exist_admin
                    print(f"Welcome {exist_admin.name} \n")
                else:
                    print("Email or password is invalid \n")
        elif option == 3:
            break
    elif current_user.is_admin:
        print("Press 1 to see all user account")
        print("Press 2 to delete any user")
        print("Press 3 to check the bank balance")
        print("Press 4 to check total loan amount")
        print("Press 5 to check the loan feature")
        print("Press 6 to on or off the loan feature")
        print("Press 7 to bankrupt")
        print("Press 8 to Sign out \n")
        option = int(input("Enter here: "))
        if option == 1:
            bank.show_all_customer_account()
        elif option == 2:
            email = input("Enter user email: ")
            bank.delete_customer_account(email)
        elif option == 3:
            print(bank.balance)
        elif option == 4:
            print(bank.total_loan_amount)
        elif option == 5:
            bank.loan_available()
        elif option == 6:
            bank.swap_loan_available()
        elif option == 7:
            bank.bankrupt = current_user
        elif option == 8:
            current_user = None
    else:
        print("Press 1 to deposit money")
        print("Press 2 to withdraw money")
        print("Press 3 to check balance")
        print("Press 4 to check transaction history")
        print("Press 5 to transfer money")
        print("Press 6 to take loan")
        print("Press 7 to Sign Out \n")
        option = int(input("Enter here: "))
        print("\n")
        if option == 1:
            if bank.bankrupt:
                print("Bank is bankrupt \n")
            else:
                money = int(input("Enter amount: "))
                print("\n")
                deposit = current_user.deposit_money(money)
                if deposit:
                    print(f"{money} TK deposit successfully \n")
                else:
                    print("Invalid amount \n")
        elif option == 2:
            amount = int(input("Enter amount: "))
            print("\n")
            if bank.bankrupt:
                print("Bank is bankrupt \n")
            else:
                current_user.withdraw_money(amount)
        elif option == 3:
            print(f"Available balance {current_user.balance} TK \n")
        elif option == 4:
            current_user.check_transaction_history()
            print("\n")
        elif option == 5:
            amount = int(input("Enter transfer amount: "))
            print("\n")
            receiver_email = input("Enter receiver email: ")
            print("\n")
            bank.transfer_money(amount, current_user, receiver_email)
        elif option == 6:
            amount = int(input("Enter loan amount: "))
            bank.take_loan(amount, current_user)
        elif option == 7:
            current_user = None
