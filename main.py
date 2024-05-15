from Bank import Bank
from Users import Admin, User
from utilities import auth
from demo_data import demo_data


c_bank = Bank("CB Bank", 10000000)
cur_user = None
isFirstTime = False

# for testing purpose
demo_data(c_bank, User, Admin)
while True:
    try:
        while True:
            if cur_user is None:
                cur_user = auth(c_bank, Admin, User)
                isFirstTime = True

            else:
                if isFirstTime:
                    print("------------------------------")
                    print(f"Welcome {cur_user.name}")
                    print("------------------------------")
                    isFirstTime = False
                if cur_user.role == "user":
                    if not isFirstTime:
                        print("------------------------------")
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
                        cur_user.deposit_money(amount, c_bank)
                    elif op == 2:
                        if not c_bank.isBankrupt:
                            amount = int(input("Enter the amount: "))
                            cur_user.withdraw_money(amount, c_bank)
                        else:
                            print("Bank is Bankrupt")
                    elif op == 3:
                        print(f"Your current balance is {cur_user.get_balance} BDT")
                    elif op == 4:
                        cur_user.get_transaction_history()
                    elif op == 5:
                        if not c_bank.isBankrupt:
                            acc_num = input("Enter Reciever's Account Number: ")
                            reciever = c_bank.find_an_user(acc_num)
                            if reciever:
                                amount = int(input("Enter the Amount: "))
                                cur_user.transfer_money(amount, reciever, c_bank)
                                c_bank.target_user = None
                            else:
                                print("This account does not exist")
                        else:
                            print("Bank is Bankrupt")
                    elif op == 6:
                        if not c_bank.isBankrupt:
                            if c_bank.isLoanOn:
                                amount = int(input("Enter the amount: "))
                                cur_user.take_loan(amount, c_bank)
                            else:
                                print("Loan is not available right now")
                        else:
                            print("Bank is Bankrupt")
                    elif op == 7:
                        cur_user.show_account_number()
                    elif op == 8:
                        cur_user = None
                        isFirstTime = True
                    else:
                        print("Invalid Option")

                elif cur_user.role == "admin":
                    if not isFirstTime:
                        print("------------------------------")
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
                        cur_user.delete_an_user(c_bank.users, account_number)
                    elif op == 2:
                        cur_user.show_all_users(c_bank)
                    elif op == 3:
                        cur_user.get_bank_balance(c_bank)
                    elif op == 4:
                        cur_user.check_total_loan(c_bank)
                    elif op == 5:
                        cur_user.switch_loan_status(c_bank)
                    elif op == 6:
                        cur_user.declare_bankruptcy(c_bank)
                    elif op == 7:
                        cur_user = None
                        isFirstTime = True
                    else:
                        print("Invalid Option")
    except Exception as e:
        print("---------------------------------------")
        print(f"An error occurred: {type(e).__name__}")
