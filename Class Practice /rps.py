# Incorporate the random library
from multiprocessing import RLock
import random

# Print Title
print("Let's Play Rock Paper Scissors!")

# Specify the three options
options = ["r", "p", "s"]

# Computer Selection
computer_choice = random.choice(options)

# User Selection
user_choice = input("Make your Choice: (r)ock, (p)aper, (s)cissors? ")

# Run Conditionals
r = "rock"
p = "paper"
s = "scissors"


if user_choice == "r" and computer_choice == "s": 
    print("You win")
elif user_choice == "r" and computer_choice == "p":
    print("You lose")
elif user_choice == "p" and computer_choice == "r":
    print("You win")
elif user_choice == "p" and computer_choice == "s":
    print("You lose")
elif user_choice == "s" and computer_choice =="p":
    print("You win")
elif user_choice == "s" and computer_choice == "r":
    print("You lose")
else:
    print("You tied")
    print("cuputer choice: " + computer_choice)
    