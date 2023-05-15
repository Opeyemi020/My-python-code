def even_number(lst):
    even_num = []
    for num in lst:
        if num % 2 == 0:
            even_num.append(num)
    return even_num


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(even_number(my_list))
