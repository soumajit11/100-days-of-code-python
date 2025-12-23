import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
option = [rock,paper,scissors]
comp_choice = random.randint(0,2)
print(f"You chose:\n{option[user_choice]}\nComputer chose:\n{option[comp_choice]}")
if user_choice == 0:
    if comp_choice == 0:
        print("Draw!")
    elif comp_choice == 1:
        print("Computer Win!")
    else:
        print("You Win!")
elif user_choice == 1:
    if comp_choice == 0:
        print("You Win!")
    elif comp_choice == 1:
        print("Draw!")
    else:
        print("Computer Win!")
else:
    if comp_choice == 0:
        print("Computer Win!")
    elif comp_choice == 1:
        print("You Win!")
    else:
        print("Draw!")
