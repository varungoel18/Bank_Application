from BankAccount import BankAccount


class SavingAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance=0.0):
        super().__init__(account_number,account_holder,balance)

    def deposit(self,amount):
        interest = amount * 0.03
        super().deposit(amount + interest)