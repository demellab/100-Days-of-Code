print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0

if size == "S":
    total_bill = 15
    print("Price of a Small Pizza is: $15")

    if pepperoni == "Y":
        total_bill += 2
    print(f"Total bill for your pizza is: {total_bill}")

elif size == "M":
    total_bill = 20
    print("Price of a Medium Pizza is: $20")

    if pepperoni == "Y":
        total_bill += 3
    print(f"Total bill for your pizza is: {total_bill}")
else:

    total_bill = 25
    print("Price of a Large Pizza is: $25")
    if pepperoni == "Y":
        total_bill += 3
    print(f"Total bill for your pizza is {total_bill}")