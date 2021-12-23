from Art import logo
import os

print(logo)
should_continue = True
max_bidding = 0
bidding_person = ""
bids = {}

while should_continue:
    name = input("what is your name ?\n")
    price = int(input("what is your bid ?\n"))
    if price > max_bidding:
        max_bidding = price
        bidding_person = name
    bids[name] = price
    response = input("Is there any other person to bid ? Type 'yes' if present otherwise 'no': ").lower()
    if response == 'no':
        should_continue = False
        print(f"The highest bid is Rs.{max_bidding} by {bidding_person}")
    else:
        os.system('cls')
        
