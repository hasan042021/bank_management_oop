def auth(bank, Admin_Class, User_Class):
    print("------------------------------------------------")
    print("You are not Logged In. Please Login or Register.")
    print("Press 1 for register")
    print("Press 2 for Login")
    ch = int(input("Enter your choice: "))
    print("------------------------------------------------")
    if ch == 1:
        print("Press 1 for User Account")
        print("Press 2 for Admin Account")
        acc = int(input("Enter your choice: "))
        u_name = input("Enter your name: ")
        u_email = input("Enter your email: ")
        u_address = input("Enter your address: ")
        u_password = input("Enter your password: ")
        if acc == 1:
            u_type = int(
                input("Account Type - savings(1) or current(2)? Type in the number: ")
            )
            user = User_Class(
                u_name,
                u_email,
                u_address,
                u_password,
                "savings" if u_type == 1 else "current",
            )
            bank.add_user(user)
            user.show_account_number()
            return user
        if acc == 2:
            admin = Admin_Class(u_name, u_email, u_address, u_password)
            bank.add_admin(admin)
            return admin
    elif ch == 2:
        ty = input("Login as user/admin - type 'u' or 'a'\n type -- ")
        isOkay = False
        if ty == "u":
            account_number = input("Enter your account number: ")
            password = input("Enter your password: ")
            for user in bank.users:
                if user.account_number == account_number and user.password == password:
                    return user
        elif ty == "a":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            for admin in bank.admins:
                if admin.email == email and admin.password == password:
                    return admin
        if not isOkay:
            print("Could not find an account. Try again")


def user_functionalities(bank, user):
    print("Press 1 to Deposit Cash.")
    print("Press 2 for Cash Withdrawal.")
    print("Press 3 to Check Your Balance.")
    print("Press 4 to See Your Transaction History.")
    print("Press 5 to Transfer Money.")
    print("Press 6 to Take A Loan.")
    print("Press 7 to show my account number.")
    print("Press 8 to Logout")
    op = int(input("Enter Your Choice: "))
    if op == 1:
        amount = int(input("Enter the amount: "))
        user.deposit_money(amount, bank)
        return user, False
    elif op == 2:
        if not bank.isBankrupt:
            amount = int(input("Enter the amount: "))
            user.withdraw_money(amount, bank)
        else:
            print("Bank is Bankrupt")
        return user, False
    elif op == 3:
        print(f"Your current balance is {user.get_balance} BDT")
        return user, False
    elif op == 4:
        user.get_transaction_history()
        return user, False
    elif op == 5:
        if not bank.isBankrupt:
            acc_num = input("Enter Reciever's Account Number: ")
            reciever = bank.find_an_user(acc_num)
            if reciever:
                amount = int(input("Enter the Amount: "))
                user.transfer_money(amount, reciever, bank)
                bank.target_user = None
            else:
                print("This account does not exist")
        else:
            print("Bank is Bankrupt")
        return user, False
    elif op == 6:
        if not bank.isBankrupt:
            if bank.isLoanOn:
                amount = int(input("Enter the amount: "))
                user.take_loan(amount, bank)
            else:
                print("Loan is not available right now")
        else:
            print("Bank is Bankrupt")
        return user, False
    elif op == 7:
        user.show_account_number()
        return user, False
    elif op == 8:
        return None, True
    else:
        print("Invalid Option")
        return user, False


def admin_functionalities(bank, user):
    print("Press 1 to Delete Any User Account .")
    print("Press 2 to See All Users Accounts.")
    print("Press 3 to Check Total Available Balance of the bank.")
    print("Press 4 to Check Total Loan Amount.")
    print("Press 5 to Change Status for Loan.")
    print("Press 6 to Change Status for Bankruptcy.")
    print("Press 7 to Logout")
    op = int(input("Enter Your Choice: "))
    if op == 1:
        account_number = input("Enter user account number: ")
        user.delete_an_user(bank.users, account_number)
        return user, False
    elif op == 2:
        user.show_all_users(bank)
        return user, False
    elif op == 3:
        user.get_bank_balance(bank)
        return user, False
    elif op == 4:
        user.check_total_loan(bank)
        return user, False
    elif op == 5:
        user.switch_loan_status(bank)
        return user, False
    elif op == 6:
        user.declare_bankruptcy(bank)
        return user, False
    elif op == 7:
        return None, True
    else:
        print("Invalid Option")
        return user, False
