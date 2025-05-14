import random

game = ["Rock", "Paper", "Scissors"]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors. "))
computer_choice = random.choice(game)

if user_choice < 0 or user_choice > 2:
    print("You've entered an invalid number. You lose!")
else:
    print(f'You chose {game[user_choice]}\n')
    print(f'Computer chose: {computer_choice}')

if user_choice == 0:
    if computer_choice == "Rock":
        print("It's a draw.")
    elif computer_choice == "Paper":
        print("You lose.")
    else:
        print("You win!")
elif user_choice == 1:
    if computer_choice == "Rock":
        print("You win!")
    elif computer_choice == "Paper":
        print("It's a draw.")
    else:
        print("You lose.")
elif user_choice == 2:
    if computer_choice == "Rock":
        print("You lose.")
    elif computer_choice == "Paper":
        print("You win!")
    else:
        print("It's a draw")
