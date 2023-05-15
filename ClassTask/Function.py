def lst(list3):
    for row in range(len(list3)):
        for arr in range(len(list3)):
            if list3[row] == list3[arr]:
                return f"{list3[row]} is a duplicate"
            else:
                return f"it is not a duplicate"


myList = ["su", "ma", "tm", "su"]
print(lst(myList))
