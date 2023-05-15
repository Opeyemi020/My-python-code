def discount(amount):
    discount = 0.1 * amount
    new_price = amount - discount
    print("discount is: ", discount, "The new price is ", new_price)


amount = int(input("Enter amount: "))
discount(amount)