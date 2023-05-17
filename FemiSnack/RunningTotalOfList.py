def the_running_total(array):
    running_total = [array[0]]
    for num in range(1, len(array)):
        running_total.append(running_total[num - 1] + array[num])
    return running_total


numbers = [1, 2, 3, 4, 5]
running_total = the_running_total(numbers)
print("Running total: ", running_total)
