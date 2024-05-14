class Bank:
    def __init__(self, name, total_balance) -> None:
        self.name = name
        self.__total_balance = total_balance
        self.isLoanOn = True
        self.isBankrupt = False
        self.admins = []
        self.users = []
        self.transactions = []
        self.__loan = 0
        self.target_user = None

    def add_user(self, user):
        self.users.append(user)

    def add_admin(self, admin):
        self.admins.append(admin)

    @property
    def get_total_loan(self):
        return self.__loan

    @get_total_loan.setter
    def add_to_loan(self, amount):
        self.__loan += amount

    @property
    def get_total_balance(self):
        return self.__total_balance

    @get_total_balance.setter
    def add_balance(self, amount):
        self.__total_balance += amount

    @get_total_balance.setter
    def remove_balance(self, amount):
        self.__total_balance -= amount

    def find_an_user(self, account_number):
        for user in self.users:
            if user.account_number == account_number:
                self.target_user = user
        return self.target_user
