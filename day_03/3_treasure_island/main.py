import art
print(art.logo)
print("Welcome to Treasure Island.")
print("Your mission is to find the tresure.")
choice1 = input("You are at a crossroad, where do you want to go? Type (left) or (right).\n").lower()
if choice1 == "left":
    choice2 = input("You have come to a lake. There is an island in the middle of the lake. Type (wait) to wait for a boat. or (swim) to swim across.\n").lower()
    if choice2 == "wait":
        choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue.\n" \
        "Which colour do you choose?\n").lower()
        if choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice3 == "yellow":
            print("You found the treasure! You Win!")
        else: 
            print("You enter a room full of snakes. Game Over.")
    else:
        print("You got attacked by sharks. Game Over.")
else:
    print("You fell into a hole. Game Over.")