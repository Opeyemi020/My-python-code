language = input("Enter preferred language")
match language:
    case "java":
        print("you are a hardcore programmer")
    case "javaScript":
        print("you are a full stark developer")
    case "python":
        print("you are an amazing programmer")
    case _:
        print("if you are learning programming for the first time,learn python")

if language == "java":
    print("you are a hardcore programmer")
elif language == "javaScript":
    print("you are a full stark developer")
elif language == "python":
    print("you are an amazing programmer")
else:
    print("if you are learning programming for the first time,learn python")

