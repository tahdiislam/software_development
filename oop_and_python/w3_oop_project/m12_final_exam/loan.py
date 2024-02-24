class Loan:
    def __init__(self, amount, receiver, loan_taking_reason="") -> None:
        self.amount = amount
        self.receiver = receiver
        self.loan_taking_reason = loan_taking_reason
        self.status = "processing"

    @property
    def success(self):
        self.status = "success"

    @property
    def failed(self):
        self.status = "failed"

    def __repr__(self) -> str:
        return f"Loan receiver: {self.receiver.name}, loan amount: {self.amount}, status: {self.status}"
