import random

rand = random.randint(1, 10)

numbers = int(input("Enter your lucky number\n"))

while numbers != rand:
    numbers = int(input("incorrect number, keep entering number\n"))


else:
    print("Congratulations!! you get the correct number")
