from random import sample

base = 3
side = base * base


def pattern(range, c):
    return (base * (range % base) + range // base + c) % side


def shuffle(s):
    return sample(s, len(s))


col = range(base)
rows = [cast * base + range for cast in shuffle(col) for range in shuffle(col)]
cols = [getter * base + column for getter in shuffle(col) for column in shuffle(col)]
num = shuffle(range(1, base * base + 1))
board = [[num[pattern(rol, col)] for col in cols] for rol in rows]
for line in board: print(line)
var = [6, 2, 5, 8, 4, 3, 7, 9, 1]
var = [7, 9, 1, 2, 6, 5, 4, 8, 3]
var = [4, 8, 3, 9, 7, 1, 6, 2, 5]
var = [8, 1, 4, 5, 9, 7, 2, 3, 6]
var = [2, 3, 6, 1, 8, 4, 9, 5, 7]
var = [9, 5, 7, 3, 2, 6, 8, 1, 4]
var = [5, 6, 9, 4, 3, 2, 1, 7, 8]
var = [3, 4, 2, 7, 1, 8, 5, 6, 9]
var = [1, 7, 8, 6, 5, 9, 3, 4, 2]
