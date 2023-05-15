def sort_list(lst=[]):
    lst = [25, 10, 15, 5, 30, 55, 35, 45]
    for minimum in range(len(lst)):
        for maximum in range(minimum + 1, len(lst)):
            if lst[maximum] < lst[minimum]:
                total = lst[minimum], lst[maximum] = lst[maximum], lst[minimum]
                return total;


print(sort_list(lst=[]))
