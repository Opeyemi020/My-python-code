def odd_number(lst):
    odd_num = []
    for num in lst:
        if num % 2 == 1:
            odd_num.append(num)
    return odd_num


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(odd_number(my_list))
