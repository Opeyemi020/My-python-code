def divisible_3(userInput: int):
    if userInput % 3 == 0: return "Fizz"
    if userInput % 5 == 0: return "Buzz"
    if userInput % 5 == 0 & userInput % 3 == 0: return "Fizz Buzz"


for i in range(1, 101):
    print(i, divisible_3(i))
