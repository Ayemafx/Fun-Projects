Name = input("Type your name:")
print(f"Welcome {Name} to this adventure")

answer = input("You are on a dirt road, it has come to an end and you can go left or right which way would you like to go?").lower()
if answer == "left":
    ques = input("You come to a river, you can walk around it or swim across? Choose walk or swim:").lower()
    if ques == "swim":
        print("You swam across and got eaten by an alligator")
    if ques == "walk":
        print("You walked for many whiles, ran out of water and you lost the game")
    else:
        print("Not valid. You lose")


elif answer == "right":
    ques = input("You come across a bridge, it looks wobbly. Do you want to cross it or head back(cross/back)?").lower()
    if ques == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (Yes/No)").lower()
        if answer == "yes":
            print("You talk to the stranger and they give you gold. You win")
        elif answer == "no":
            print("You ignore the stranger, they are offended. You lose")
        else:
            print("Not Valid. You lose")

    elif ques == "back":
        print("You go back and loose")
    else:
        print("Not Valid. You lose")

else:
    print("Not valid option.You Lose")

print("Thank You for trying", Name)

