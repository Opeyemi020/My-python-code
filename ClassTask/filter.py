list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def odd_value(index):
    if index % 2 != 0:
        return index


print(list(filter(odd_value, list3)))
