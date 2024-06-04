import os
import platform

from art import logo

bids = {}
bidding_finished = False


def clear_console():
    # Check the OS and clear the console accordingly
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")
    # Print multiple newlines as a fallback
    print("\n" * 100)


def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Winner is {winner} with a bid of ${highest_bid}.")


print(logo)
print("Welcome to the secret auction program")

while not bidding_finished:
    names = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[names] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no.\n").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        clear_console()
