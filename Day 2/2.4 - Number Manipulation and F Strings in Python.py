print(int(8 / 3))
print(8 / 3)
print(round(8 / 3))
print(round(8 / 3, 2))
print(round(2.666666, 2))
print(8 // 3)

result = 4 / 2
result /= 2
print(result)

score = 0

# User scores a point
score += 1
height = 1.8
isWinning = True
print(score)

print("Your score is " + str(score))

# f-String
print(f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#
# Create a program using maths and f-Strings that tells us how many weeks we have left, if we live until 90 years old.
#
# It will take your current age as the input and output a message with our time left in this format:
#
# You have x weeks left.
# Where x is replaced with the actual calculated number of weeks the input age has left until age 90.

# Example Input
# 56
# Example Output
# You have 1768 weeks left.


age = input()
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
years = 90 - int(age)
weeks = years * 52

print(f"You have {weeks} weeks left.")
