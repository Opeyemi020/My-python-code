with open("record2.txt", mode='w') as file:
    file.write("005 hyelnati 75\n")
    file.write("006 segun 75\n")
    file.write("007 Esther 75\n")

with open("product.txt", mode='w') as file:
    file.write("10389 kulitech 100\n")
    file.write("11234 Always 900\n")
    file.write("10234 Boyboy 3000\n")
    file.write("10083 nutri milk 100\n")
    file.write("10378 Cascade water 200\n")

with open("record2.txt", mode='r') as records:
    for record in records:
        num, name, score = record.split()
        print(f"{num:<10} {name:<10} {score:>10}")


