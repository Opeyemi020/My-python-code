numbers = []
for number in range(21):
    numbers.append(number)

print(numbers)
numbers = [i for i in range(21)]
for number in numbers:
    if number % 2 == 1: print(number)

for item in range(5, 12):
    numbers[item] = 0

print(numbers)
