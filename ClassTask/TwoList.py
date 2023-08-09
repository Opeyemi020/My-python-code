def common_elements(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return tuple(common)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = common_elements(list1, list2)
print(result)
