def print_zero_first_last(lst):
    if len(lst) > 0:
        lst[0] = 0
        if len(lst) > 1:
            lst[-1] = 0
    print(lst)

my_list = [1, 2, 3, 4, 5]
print_zero_first_last(my_list)
