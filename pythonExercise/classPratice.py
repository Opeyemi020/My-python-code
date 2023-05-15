import random

user_input = int(input("how many times did you want to roll it\n"))
a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
for i in range(user_input):
    rolling = random.randint(1, 7)
    if rolling == 1:
        a += 1
    if rolling == 2:
        b += 1
    if rolling == 3:
        c += 1
    if rolling == 4:
        d += 1
    if rolling == 5:
        e += 1
    if rolling == 6:
        f += 1

print(f"the amount of time 1 roll is {a} ")
print(f"the amount of time 2 roll is {b} ")
print(f"the amount of time 3 roll is {c} ")
print(f"the amount of time 4 roll is {d} ")
print(f"the amount of time 5 roll is {e} ")
print(f"the amount of time 6 roll is {f} ")
