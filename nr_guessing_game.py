#Number Guessing Game

import random as rn

print("Select desired range to for game to start")
low_range = int(input("Enter the low range: "))
high_range = int(input("Enter the high range: "))

if not isinstance(low_range, int) or not isinstance(high_range, int):
    print("You need to enter numbers")
    exit()
    
selected_nr = rn.randint(low_range, high_range)
print("Number has been selected. Good luck.")

guess = None
while True:
    guess = int(input("Enter your guees: "))
    if guess not in range(low_range, high_range + 1):
        print("The number you entered is outside the selected range.")
    elif guess < selected_nr:
        print("Too low, try again!")
    elif guess > selected_nr:
        print("Too high, try again!")
    else:
        print("You got it! Number was", selected_nr)
        break
