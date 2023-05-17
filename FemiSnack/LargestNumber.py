def largest_number(array):
    largest = array[0]
    for num in array:
        if num > largest:
            largest = num
    return largest


numbers = [1, 1020]
largest = largest_number(numbers)
print("Largest number: ", largest)
