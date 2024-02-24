class Transaction:
    def __init__(self, amount, receiver_account_no, category) -> None:
        self.category = category
        self.amount = amount
        self.receiver_account_number = receiver_account_no
        self.status = "processing"

    @property
    def success(self):
        self.status = "success"

    @property
    def failed(self):
        self.status = "failed"


class Withdraw(Transaction):
    def __init__(self, amount, receiver_account_no) -> None:
        super().__init__(amount, receiver_account_no, "withdraw")

    def __str__(self) -> str:
        return f"Transaction amount: {self.amount}, category: {self.category}, receiver  AC number: {self.receiver_account_number} status: {self.status}"


class Transfer(Transaction):
    def __init__(self, amount, receiver_account_no, sender_account_no) -> None:
        self.sender_account_number = sender_account_no
        super().__init__(amount, receiver_account_no, "transfer")

    def __str__(self) -> str:
        return f"Transaction amount: {self.amount}, category: {self.category}, sender AC number: {self.sender_account_number}, receiver  AC number: {self.receiver_account_number}, status: {self.status}"
