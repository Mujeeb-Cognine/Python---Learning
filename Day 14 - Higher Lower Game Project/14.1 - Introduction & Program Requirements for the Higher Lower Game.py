import random

from art import logo, vs
from game_data import data


def format_data(account):
    """Takes the account data and return the printable format."""
    account_name = account['name']
    account_description = account['description']
    account_country = account['country']
    return f"{account_name}, a {account_description}, from {account_country}."


def check_answer(guess, a_followers, b_followers):
    """Takes the user guess and follower counts and returns if they got it right."""

    if a_followers > b_followers:
        return guess == "A"
    else:
        return guess == "B"


print(logo)

score = 0

game_should_continue = True

account_2 = random.choice(data)

while game_should_continue:

    account_1 = account_2
    account_2 = random.choice(data)

    if account_1 == account_2:
        account_2 = random.choice(data)

    print(f"Compare A: {format_data(account_1)}.")

    print(vs)

    print(f"Against B: {format_data(account_2)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").upper()

    a_follower_count = account_1['follower_count']
    b_follower_count = account_2['follower_count']

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")
