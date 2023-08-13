from BankAccount import BankAccount


class CurrentAccount(BankAccount):
    def __init__(self,account_number,account_holder,balance=0.0):
        super.__init__(account_number,account_holder,balance)

    def withdraw(self,amount):
        if self.balance >= (amount+200):
            super.withdraw(amount+200)
        else:
            print("Insufficient funds for withdrawl")
