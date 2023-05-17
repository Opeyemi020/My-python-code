rate = 0.05


def investment(year, principal):
    rate = 0.05
    for count in range(1, year + 1):
        try:
            roi = principal * rate
            future_value = principal + roi
            principal = future_value
            print(f"year {year} return on investment is {roi},your principal is now {future_value}")
        except TypeError:
            return "The amount cannot be a string"
        except ValueError:

            return "Value cannot be negative"


principal = float(input("Enter the amount you want to invest"))
year = int(input("Enter number of year: "))

investment(year, principal)
