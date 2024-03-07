import random

computer_wins = 0
user_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock, Paper, or Scissors, or Q to quit the game: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0,2)
    computer_pick = options[random_number]
    print("Computer picked ", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("Congratulations! You have defeated the computer!")
        user_wins += 1
        continue

    elif user_input == "scissors" and computer_pick == "paper":
        print("Congratulations! You have defeated the computer!")
        user_wins += 1


    elif user_input == "paper" and computer_pick == "rock":
        print("Congratulations! You have defeated the computer!")
        user_wins += 1

    elif user_input == computer_pick:
        print("This round is a tie!")

    else:
        print("The computer has defeated you!")
        computer_wins += 1






print("you won", user_wins, "times")
print("the computer won", computer_wins, "times")
if computer_wins > user_wins:
    print("The computer has defeated you in this game.")

elif user_wins == computer_wins:
    print("it is a tie!")

else:
    print("you have crushed the computer.")



print("goodbye!")