print("Welcome to Treasure Island")
print("Your mission is to find the treasure")

option_1 = input("Would you like to go Left/Right: ")
if option_1 == "right" or option_1 == "Right":
    print("Game over")

option_2 = input("Would you like to Swim/Wait: ")
if option_2 == "Swim" or option_2 == "swim":
    print("Sorry. Game over!")

option_3 = input("Which door?")
if option_3 == "Red" or option_3 == "Blue":
    print("Sorry! Game over")

else:
    print("You win")