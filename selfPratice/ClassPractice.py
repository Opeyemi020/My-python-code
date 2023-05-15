# list unpacking
num = [1, 2, 3, 4, 5]
num[0] = 10
num[4] = 555
print(num)
print(len(num))

numbers = [1, 2, 3, 4, 5]
x, y, z, a, b, = numbers
x, *others, y = numbers
print(y)

# x, y, *others = numbers
# print(others)
print(y)
name = numbers[::-1]
print(name)

letters = list("Hello baby")
print(letters)

for index, letter in enumerate(letters):
    print(index, letter)



# def multiply(x: int, y: int) -> int:
#     return x * y
#
# # def multiply_with_more_args =
