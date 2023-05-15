num1 = float(input("Enter the time the first person needed to complete the course\n"))
num2 = float(input("Enter the time the second person needed to complete the course\n"))
num3 = float(input("Enter the time the third person needed to complete the course\n"))

num = num1, num2, num3
print(sorted(num))

if num1 <= num2 and num1 <= num3:
    # smallest = num1
    if num2 <= num3:
        smallest = num1, middle = num2, largest = num3
elif num2 <= num1 and num2 <= num3:
    # smallest = num2
    if num1 <= num2:
        smallest = num2, middle = num1, largest = num3
elif num3 <= num2 and num3 <= num1:
    # smallest = num3
    if num2 <= num1:
        smallest = num3, middle = num2, largest = num1
    else:
        arranged = num3, num1, num2
print(f"The ascending order is {arranged} ")
