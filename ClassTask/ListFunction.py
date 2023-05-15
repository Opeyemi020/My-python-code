list2 = [1, 2, 3, 4, 5, 6]


def square_number(i):
    return i ** 2


ans = list(map(square_number, list2))
print(ans)
