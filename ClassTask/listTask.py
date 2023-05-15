name = ["sultan", "Opeyemi"]
count = 0
while count < 5:
    user_input = input("Enter a name\n")
    print(user_input)
    if 8 <= len(user_input) and len(user_input) > 0:
        print("Enter name less than eight letters")
        name.append(user_input)
    count += 1

    print(name)

