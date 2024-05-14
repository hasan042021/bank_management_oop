from Transaction import WithDraw, Deposit, TakeLoan, TransferMoney
from random import randint


class Account:
    def __init__(self, name, email, address, password) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.password = password

    @staticmethod
    def generate_random_int():
        return randint(1000000000, 9999999999)


class User(Account):
    def __init__(self, name, email, address, password, account_type) -> None:
        super().__init__(name, email, address, password)
        self.__balance = 0
        self.account_number = str.upper(self.name[:3]) + str(
            Account.generate_random_int()
        )
        self.account_type = account_type
        self.role = "user"
        self.available_loans = 2
        self.transactions = []
        self.my_transaction_info = {
            "account_number": self.account_number,
            "email": self.email,
        }

    @property
    def get_balance(self):
        return self.__balance

    @get_balance.setter
    def add_balance(self, amount):
        self.__balance += amount

    @get_balance.setter
    def decrease_balance(self, amount):
        self.__balance -= amount

    def get_transaction_history(self):
        for transaction in self.transactions:
            if transaction.type == "Transfer":
                print(
                    f"Transaction ID:{transaction.transaction_id} Transaction type: {transaction.type} Amount: {transaction.amount}  Reciever: {transaction.reciever}"
                )
            else:
                print(
                    f"Transaction ID:{transaction.transaction_id}, Transaction type: {transaction.type}, Amount:{transaction.amount}"
                )

    def take_loan(self, amount, bank):
        if self.available_loans:
            self.add_balance = amount
            transaction = TakeLoan(self.my_transaction_info, amount)
            bank.transactions.append(transaction)
            self.transactions.append(transaction)
            bank.add_to_loan = amount
            self.available_loans -= 1
        else:
            print("You have exceeded your limit. You can not take more loans.")

    def transfer_money(self, amount, reciever, bank):
        if amount <= self.get_balance:
            self.decrease_balance = amount
            reciever_transaction_info = {
                "account_number": reciever.account_number,
                "email": reciever.email,
            }
            transaction = TransferMoney(
                self.my_transaction_info, reciever_transaction_info, amount
            )
            bank.transactions.append(transaction)
            self.transactions.append(transaction)
            reciever.transactions.append(transaction)
        else:
            print("You have not enough money in your account")

    def withdraw_money(self, amount, bank):
        if amount <= self.get_balance:
            self.decrease_balance = amount
            transaction = WithDraw(self.my_transaction_info, amount)
            bank.remove_balance = amount
            bank.transactions.append(transaction)
            self.transactions.append(transaction)
        else:
            print("Withdrawal Amount Exceeded")

    def deposit_money(self, amount, bank):
        self.add_balance = amount
        transaction = Deposit(self.my_transaction_info, amount)
        bank.add_balance = amount
        bank.transactions.append(transaction)
        self.transactions.append(transaction)

    def show_account_number(self):
        print(f"My Account Number is: {self.account_number}")


class Admin(Account):
    def __init__(self, name, email, address, password) -> None:
        super().__init__(name, email, address, password)
        self.role = "admin"

    def show_all_users(self, bank):
        for user in bank.users:
            print(
                f"{user.account_number} - {user.name} - {user.email} - {user.get_balance}BDT"
            )

    def delete_an_user(self, users, account_number):
        for i, user in enumerate(users):
            if user.account_number == account_number:
                users.remove(users[i])
                print("User Deleted Successfully")

    def get_bank_balance(self, bank):
        print(f"Total balance of {bank.name} - {bank.get_total_balance}BDT")

    def switch_loan_status(self, bank):
        bank.status = not bank.status
        print("Loan status changed")

    def check_total_loan(self, bank):
        print(bank.get_total_loan)

    def declare_bankruptcy(self, bank):
        bank.isBankrupt = not bank.isBankrupt
        print("Bankruptcy status changed")
