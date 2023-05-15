list1 = list(range(1, 21))
print(list1)

odd_numbers = list1[::2]
print(odd_numbers)
print(list1)

list1[5:11] = [0] * len(list1[5:11])
print(list1)

first_seven = list1[:7]
print(first_seven)

list1[:] = []
print(list1)
