print("hour\tNumber of bacteria")
print("0\t\t200")
print("5\t\t6400")
print("10\t\t204800")
print("15\t\t6553600")

print("{:<5} {:<20}".format("Hour", "Number of bacteria"))
print("{:<5} {:>5} {:>5} {:<5}".format("0", " ", " ", "200"))
print("{:<5} {:>5} {:>5} {:<5}".format("5", " ", " ", "6400"))
print("{:<5} {:>5} {:>5} {:<10}".format("10", " ", " ", "204800"))
print("{:<5} {:>5} {:>5} {:<10}".format("15", ' ', ' ', "6553600"))