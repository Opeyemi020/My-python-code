
rate = 0.05


def invest(year, principal):
    rate = 0.05
    for count in range(1, year+1):
        roi = principal * rate
        future_value = principal + roi
        principal= future_value
        print(f"year{year}return on investment is {roi},your principal is now {future_value}")


principal = float(input("Enter the amount you want to invest"))
year = int(input("Enter number of year: "))

invest(year, principal)