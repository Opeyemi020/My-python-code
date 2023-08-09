from decimal import Decimal


class Account:

    def __init__(self, name: str, balance: Decimal):
        self.name = name
        self.balance = balance

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative..")
        self.__balance = amount

    def __str__(self):
        return f"{self.name} {self.balance}"

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            return ValueError("Your Papa..!!, you wan scam us")
        self.balance -= amount


account1 = Account("mariam", Decimal(100.00))
print(account1)
