#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
app = Flask(__name__)

@app.route("/")


# write a game which plays rock paper and scissor game through console with user
# write a game which plays rock paper and scissor game through console with user

def play_game():
    print("Welcome to Rock Paper Scissor Game")
    print("Please enter your choice")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")
    user_choice = int(input("Enter your choice: "))
    print("Your choice is ", user_choice)
    print("Computer is choosing...")
    import random
    computer_choice = random.randint(1, 3)
    print("Computer choice is ", computer_choice)
    if user_choice == computer_choice:
        print("Game is draw")
    elif user_choice == 1 and computer_choice == 2:
        print("Computer wins")
    elif user_choice == 1 and computer_choice == 3:
        print("User wins")
    elif user_choice == 2 and computer_choice == 1:
        print("User wins")
    elif user_choice == 2 and computer_choice == 3:
        print("Computer wins")
    elif user_choice == 3 and computer_choice == 1:
        print("Computer wins")
    elif user_choice == 3 and computer_choice == 2:
        print("User wins")
    else:
        print("Invalid choice")

play_game()



