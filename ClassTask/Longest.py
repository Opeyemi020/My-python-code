def largest_number(number):
    largest = number[0]
    for item in number:
        if len(item) > len(largest):
            largest = item
    return largest, len(largest)


test_list = ['best', 'Esther', 'Emmanuel']

print(largest_number(test_list))

test_list = ['best', 'Esther', 'Emmanuel']
print("The original list : " + str(test_list))
max_len = -1
for ele in test_list:
    if len(ele) > max_len:
        max_len = len(ele)
        res = ele
print("Maximum largest element is : " + res)


from statistics import mode
name = ["ope","ope","timmy"]
com = mode(name)
print(com)


