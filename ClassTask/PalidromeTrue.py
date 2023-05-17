def check_palidrome(a: str):
    return a.lower() == a.lower()[::-1]


print(check_palidrome("Dad"))
