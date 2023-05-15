from itertools import count

rate = 0.05

def invest(year, principal):
    rate = 0.05
    while count in range(1,year+1):
        rate = 0.05
        rio = principal*rate
        future_value = principal + rio
        principal=future_value
        print(f"year{year}return on investment is {rio}your principal is now future_value")
        principal = float(input("Enter the amount you want to invest"))
        year = int(input("Enter number of year: "))

        invest(year, principal)
