import random


range_ceiling = input("Type a number: ")


if range_ceiling.isdigit():
    range_ceiling = int(range_ceiling)

    if range_ceiling <= 0:
        print("Please type a number larger than zero next time!")
        quit()
else:
    print("Please type a number next time!")
    quit()

random_number = random.randint(0,range_ceiling)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess please: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
            print("Please type a number next time!")
            continue
    if user_guess == random_number:
        print("Nice job you got it!")

        break

    elif user_guess > random_number:
            print(" You guessed too high there buddy")
    else:
            print("You guessed too low bubba!")
            print("Sorry but that is not quite right buster! Try again")


print("You got it in ", guesses ,"guesses! ")


