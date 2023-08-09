class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount} units. New balance: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount} units. New balance: {self.balance}")
        else:
            print("Insufficient funds.")

    def check_balance(self):
        print(f"Account balance: {self.balance}")

    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.deposit(amount)
            print(f"Transferred {amount} to account {recipient_account.account_number}.")
        else:
            print("Insufficient funds.")


account1 = BankAccount("8138956052")
account2 = BankAccount("9053533053", 100)

account1.deposit(500)
account2.check_balance()

account1.transfer(account2, 200)
account1.check_balance()
account2.check_balance()

account2.withdraw(50)
account2.check_balance()