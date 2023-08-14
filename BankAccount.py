class BankAccount:
    def __init__(self,account_number,account_holder,balance=0.0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount")

    def withdraw(self,amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds")

    def transfer(self,other_account,amount):
        if 0< amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
            print(f"Transferred ${amount} to account {other_account.account_number}")
        else:
            print("Insufficient balance for transfer")

    def get_balance(self):
        print(f"Account balance: ${self.balance:.2f}")