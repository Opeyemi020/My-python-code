def get_sum_of_characters(name):
    return sum([ord(char)
                for char in name])


tom = "Tom"
jim = "Jim"

tom_sum = get_sum_of_characters(tom)
jim_sum = get_sum_of_characters(jim)

if tom_sum > jim_sum:
    print('Tom goes first')
elif jim_sum > tom_sum:
    print('Jim goes first')
else:
    print("it's a tie")

print(ord('B'), (ord('C'), (ord('D')), (ord('b')),
                 (ord('c')), (ord('d')), (ord('0')),
                 (ord('1')), (ord('2')), (ord('$')),
                 (ord('*')), (ord('+')), (ord("\t"))))
