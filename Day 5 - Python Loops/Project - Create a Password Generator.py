import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

symbols = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
    '[', ']', '{', '}', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/', '\\', '|', '~', '`'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
number_of_letters = int(input("How many letters would you like in your password?\n"))
number_of_symbols = int(input("How many symbols would you like?\n"))
number_of_numbers = int(input("How many numbers would you like?\n"))

# Easy Level

# password = ""
#
# for letter in range(1, number_of_letters + 1):
#     password += random.choice(letters)
# for symbol in range(1, number_of_symbols + 1):
#     password += random.choice(symbols)
# for number in range(1, number_of_numbers + 1):
#     password += random.choice(numbers)
#
# print(f"Here is your password: {password}")

# Hard Level

password = []

for letter in range(1, number_of_letters + 1):
    password += random.choice(letters)
for symbol in range(1, number_of_symbols + 1):
    password += random.choice(symbols)
for number in range(1, number_of_numbers + 1):
    password += random.choice(numbers)

random.shuffle(password)

actual_password = ""
for char in password:
    actual_password += char

print(f"Here is your password: {actual_password}")
