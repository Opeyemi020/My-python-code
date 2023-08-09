def largest_number(array):
    largestNum = array[0]
    for num in array:
        if num > largestNum:
            largestNum = num
    return largestNum


numbers = [2, 9, 3, 1]
largest = largest_number(numbers)
print("Largest number is: ", largest)


def smallest_number(array):
    smallestNumber = array[0]
    for num in array:
        if num < smallestNumber:
            smallestNumber = num
            return smallestNumber


number = [2, 9, 3, 1];
smallest = smallest_number(number)
print("Smallest number is :", smallest)

my_array = [2, 9, 3, 1]
array_sum = sum(my_array)

print("Sum of the array:", array_sum)

digit = [2, 9, 3, 1]
print(digit[::-1])
