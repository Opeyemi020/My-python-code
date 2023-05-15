found = False
names = ['sultan','david','mariam','lateef']
for name in names:
    if name.startswith("-1"):
        print("found")
        break
    else:
        print("not found")