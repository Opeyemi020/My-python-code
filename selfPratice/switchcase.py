
def switch_case(argument):
    match argument:
        case "zero":
            return 0
        case "One":
            return 1
        case "two":
            return 2
        case "Three":
            return 3
        case _:
            return "nothing"