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
