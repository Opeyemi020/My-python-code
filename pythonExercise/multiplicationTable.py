num = 12
for index in range(1, num + 1):
    for index1 in range(1, num + 1):
        print(end=" "f'{index : >3}    *   {index1 : >3}  = {index * index1 : >3}     ')
    print()
