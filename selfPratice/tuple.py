this_tuple = ("apple", "banana", "orange")
print(this_tuple)
tuple1 = ("sultan", "timileyin", "mariam")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)
print(type(tuple2))
print(tuple1)
print(tuple2)
print(tuple3)
thistuple1 = ("apple", "banana", "cherry")
print(thistuple1[-1])
thistuple2 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple2[2:5])
thistuple3 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple3[:4])
thistuple4 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple4[2:])

thistuple5 = tuple(range(1, 51))
print(thistuple5)

index = thistuple5[0:51:2]
print(index)

index2 = thistuple5[1:51:2]
print(index2)

add = index + index2
print(add)

x, y, z, *others = thistuple5
print(x, y, z, others)

set1 = {1, 1, 1, 2, 2, 2, 3, 4, 1}
print(set1)
print(type(set1))

list1 = {1, 1, 1, 2, 2, 2, 3, 4, 1}
print(set(list1))

set2 = {1, 4, 6, 8, 9, 5}

set2.add(10)
print(set2)

if 6 not in set1:
    print("yes")