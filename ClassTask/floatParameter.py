def add_float_numbers(a, b):
    total = 0.0
    try:
        total += a + b
        print(total)
    except ValueError:
        print("Invalid input. Please enter a float number.")
    else:
        print("float total:", total)


a = 8
b = 9
print(add_float_numbers(a,b))