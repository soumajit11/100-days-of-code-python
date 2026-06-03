import os
import art
def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
print(art.logo)
blind_bid = {}
while True:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    blind_bid[name] = bid
    choice = input("Are there any other bidders? Type 'yes' or 'no'.\n" ).lower()
    clear_screen()
    if choice == "no":
        break
max_bid = 0
max_bid_name = ""
for i in blind_bid:
    if blind_bid[i]>max_bid:
        max_bid = blind_bid[i]
        max_bid_name = i
print(f"The winner is {max_bid_name} with a bid of ${max_bid}")