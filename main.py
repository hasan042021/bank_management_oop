from Bank import Bank
from Users import Admin, User
from utilities import (
    auth,
    user_functionalities,
    admin_functionalities,
)
from display_designs import header, decoration
from demo_data import demo_data


c_bank = Bank("CB Bank", 10000000)
global cur_user
cur_user = None
isFirstTime = False

# for testing purpose
demo_data(c_bank, User, Admin)


try:
    while True:
        if cur_user is None:
            cur_user = auth(c_bank, Admin, User)
            isFirstTime = True

        else:
            isFirstTime = header(cur_user, isFirstTime)

            if cur_user.role == "user":
                decoration(isFirstTime)
                cur_user, isFirstTime = user_functionalities(c_bank, cur_user)

            elif cur_user.role == "admin":
                decoration(isFirstTime)
                cur_user, isFirstTime = admin_functionalities(c_bank, cur_user)

except Exception as e:
    print("---------------------------------------")
    print(f"An error occurred: {type(e).__name__}")
    print("Error details", e)
