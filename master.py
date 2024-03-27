name = input("Type your name: ")
print(f"Welcome {name} to this adventure!")

answer = input(
    "You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? "
).lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim arcoss? Type walk or swim: "
    ).lower()

    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles, ran out of water and you lost the game.")
    else:
        print("Not a valid option. You lose.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it loos wobbly. Do you want to cross it or head back (cross/back)? "
    ).lower()
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to him (yes/no)? "
        ).lower()

        if answer == "yes":
            print("You talk to the stranger and he give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")
else:
    print("Not a valid option. You lose.")

print(f"Thank you for trying {name}!")
