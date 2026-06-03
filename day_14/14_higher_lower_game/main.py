from art import logo
from data_entry import data
import random

def check(guess, a, b):
    if a>b:
        return guess == "a"
    else:
        return guess == "b"


print(logo)
score = 0
print(f"Score = 0")
win = True
account_b = random.choice(data)
while win:
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {account_a["name"]}, a {account_a["description"]}, from {account_a["country"]}")
    print("<-----VS----->")
    print(f"Against B: {account_b["name"]}, a {account_b["description"]}, from {account_b["country"]}")
    guess = input("Who has more followers? Type 'A' or 'B':").lower()
    is_correct  = check(guess, account_a["follower_count"], account_b["follower_count"])
    if is_correct:
        score+=1
        print(f"You are right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        win = False
    print("\n\n")
