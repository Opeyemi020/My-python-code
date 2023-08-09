class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            self.accounts[account_number] = initial_balance
            print(f"Account {account_number} created with initial balance: {initial_balance}")

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount
            print(
                f"Deposited {amount} units into account {account_number}. New balance: {self.accounts[account_number]}")
        else:
            print("Invalid account number.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number] >= amount:
                self.accounts[account_number] -= amount
                print(
                    f"Withdrew {amount} units from account {account_number}. New balance: {self.accounts[account_number]}")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account number.")

    def check_balance(self, account_number):
        if account_number in self.accounts:
            print(f"Account {account_number} balance: {self.accounts[account_number]}")
        else:
            print("Invalid account number.")

    def transfer(self, sender_account, recipient_account, amount):
        if sender_account in self.accounts and recipient_account in self.accounts:
            if self.accounts[sender_account] >= amount:
                self.accounts[sender_account] -= amount
                self.accounts[recipient_account] += amount
                print(f"Transferred {amount} from account {sender_account} to receiver account {recipient_account}.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid account number.")


bank = Bank()

bank.create_account("12345", 1000)
bank.create_account("B67890")

bank.deposit("12345", 500)
bank.check_balance("12345")

bank.transfer("12345", "B67890", 200)
bank.check_balance("12345")
bank.check_balance("B67890")

bank.withdraw("B67890", 50)
bank.check_balance("B67890")
