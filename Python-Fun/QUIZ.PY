print("Welcome to the Quiz!")

play = input("Would you like to play the game? ")

if play.lower() != "yes":
    quit()

player = input("Please enter your name player!")
print("Welcome " + str(player) + "!")


print("Okay then let us get started!")
score = 0
response1 = input("Is coding fun? ")
if response1.lower() == "yes":
    print( "correct, swell job.")
    score +=1
else:
    print("Incorrect!!!!")

response2 = input("What is the best sport to watch? " ).lower()
if response2.lower() == "football":
    print( "correct, swell job.")
    score += 1
else:
    print("Incorrect!!!!")

response3 = input("What does CLI stand for? " ).lower()
if response3 == "command line interface":
    print( "correct, swell job.")
    score += 1
else:
    print("Incorrect!!!!")

response4 = input("What language are game script codes written in? " ).lower()
if response4 == "c++":
    print( "correct, swell job.")
    score += 1
else:
    print("Incorrect!!!!")

print("you got " + str(score) + " questions right!")
print("you got " + str((score/4)*100) + "%")