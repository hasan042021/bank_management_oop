from datetime import datetime


class Transaction:
    cur_time = datetime.now()
    unformatted_string = cur_time.strftime("%Y%m%d%H%M%S%f")

    def __init__(self, requester, amount) -> None:
        self.requester = requester
        self.amount = amount
        self.transaction_id = str.upper(
            self.unformatted_string + self.requester["email"][:3]
        )

    def __repr__(self) -> str:
        if self.type == "Transfer":
            return f"{self.transaction_id}   { self.requester['account_number']}  {self.reciever['account_number']} {self.amount}"
        else:
            return f"{self.transaction_id}  {self.requester['account_number']}  {self.amount}"


class Deposit(Transaction):
    def __init__(self, requester, amount) -> None:
        super().__init__(requester, amount)
        self.type = "Deposit"


class WithDraw(Transaction):
    def __init__(self, requester, amount) -> None:
        super().__init__(requester, amount)
        self.type = "Withdraw"


class TransferMoney(Transaction):
    def __init__(self, requester, reciever, amount) -> None:
        super().__init__(requester, amount)
        self.reciever = reciever
        self.type = "Transfer"


class TakeLoan(Transaction):
    def __init__(self, requester, amount) -> None:
        super().__init__(requester, amount)
        self.type = "Loan"
