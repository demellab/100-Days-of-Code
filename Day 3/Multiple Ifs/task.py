print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
total_bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        total_bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        total_bill = 7
        print("Youth tickets are $7")
    else:
        total_bill = 12
        print("Adult tickets are $12.")

    pic_please = input("Do you want a photo taken: Y/N?")
    if pic_please == "Y":
        total_bill = total_bill + 3

    print(f"Your final bill is: ${total_bill}. Please pay at the counter!")

else:
    print("Sorry you have to grow taller before you can ride.")
