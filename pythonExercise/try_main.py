from account import Account
from decimal import Decimal

account1 = Account("mariam",Decimal(100.00))
if __name__ == '__main__':
    print(account1.name)