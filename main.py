from CurrentAccount import CurrentAccount
from SavingAccount import SavingAccount


def main():
    global account_number, account_holder
    accounts = {}
    while True:
        print("1. Create savings account")
        print("2. Create Current account")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Transfer")
        print("6. Check Balance")
        print("7. Exit")
        choice = int(input("Enter your choice:"))

        if choice == 1 or choice == 2:
            account_number = input("Enter the account number: ")
            account_holder = input("Enter account holder name: ")

            if choice == 1:
                accounts[account_number] = SavingAccount(account_number, account_holder)
                print("Saving account Created")

        elif choice == 2:
            accounts[account_number] = CurrentAccount(account_number, account_holder)
            print("Current account created")

        elif choice == 3:
            account_number = input("Enter the account number: ")
            if account_number in accounts:
                amount = float(input("Enter the deposit amount: "))
                accounts[account_number].deposit(amount)
            else:
                print("account not found")

        elif choice == 4:
            account_number = input("Enter the account number: ")
            if account_number in accounts:
                amount = float(input("Enter the withdrawl amount"))
                accounts[account_number].withdraw(amount)
            else:
                print("Account not found")

        elif choice == 5:
            account_number1 = input("Enter the source account number: ")
            account_number2 = input("Enter the destination account number: ")
            if account_number1 in accounts and account_number2 in accounts:
                amount = float(input("Enter the transfer amount: "))
                accounts[account_number1].transfer(accounts[account_number2], amount)

            else:
                print("One or both accounts not found")

        elif choice == 6:
            account_number = input("Enter the account number: ")
            if account_number in accounts:
                accounts[account_number].get_balance()
            else:
                print("Account not found")

        elif choice == 7:
            print("Exiting..")
            break

        else:
            print("Invalid choice,please try again")


if __name__ == "__main__":
    main()
