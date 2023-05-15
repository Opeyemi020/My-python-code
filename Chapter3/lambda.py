list2 = [1, 2, 3, 4, 5, 6]
list3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def square(n):
    return n ** 2


ans = list(map(square, list2))
print(ans)


def odd_num(lzt):
    odd = []
    for n in lzt:
        if n % 2 != 0:
            odd.append(n)

    return odd


print(odd_num(list3))


def odd_value(n):
    if n % 2 != 0:
        return n


print(list(filter(lambda n: n % 2 != 0, list3)))
print(list(filter(lambda n: n ** 2,list3)))
