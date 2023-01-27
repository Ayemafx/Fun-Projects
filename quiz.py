print("Welcome to my quiz!")
play = input("Do you want to play the game?")
if play.lower() != "yes":
    quit()
score = 0
print("Okay lets play")
answer = input("What does a CPU stand for?")
if answer.lower() == "central processing unit":
    print("Your answer is correct")
    score += 1
else:
    print('Incorrect!')

answer = input("What does a RAM stand for?")
if answer.lower() == "random access memory":
    print("Your answer is correct")
    score += 1
else:
    print('Incorrect!')

answer = input("What does a GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("Your answer is correct")
    score += 1
else:
    print('Incorrect!')
answer = input("What does a PSU stand for?")
if answer.lower() == "power supply":
    print("Your answer is correct")
    score += 1
else:
    print('Incorrect!')
print("Your score is" + " " + str(score))