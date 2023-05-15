def username_Generator(email):
    username = ""
    for username in email:
        if email != "@":
            username += email
        else:
            break
        return username


print(f"enter your email")
print(f"your user name is ", username_Generator())
