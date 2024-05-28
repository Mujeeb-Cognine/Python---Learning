print(input())
print(input())
print(input())

# Inputs

# Jane
# Ben
# Tom
# ----------------------------------------------------------------
# Without changing the demo code, trying clicking Submit using the current code.
#
# See how we can use hidden inputs to create lots of tests to see if your code is correct.

num1 = int(input())
num2 = int(input())

print(num1 * num2)

# ----------------------------------------------------------------
# If a student didn't complete the coding exercise, then the extra tests should catch this.
#
# For example in this case 6 is the correct answer for the visible inputs. But behind the scenes when you submit the
# code we are also passing in 5 and 5.
#
# 5 x 5 = 25
#
# while
#
# 2 x 3 = 6
#
# So the only way for the student to pass all the tests in the evaluation is to write the correct code.
#
# This is how we ensure you're doing the right things and test your understanding of the programming concepts. It's
# like having a teacher next to you checking your code.

num1 = int(input())
num2 = int(input())

print(6)

# Inputs

# 2
# 3

# Correct Code
print(num1 * num2)

# ----------------------------------------------------------------
# Try it yourself. Print the input text into the output area.

# Input

# Change this

print(input())

numOfLetters = len("Angela")
print(numOfLetters)

# ----------------------------------------------------------------
# Write a program that calculates and outputs the number of characters in any name. The automated tests will try out
# lots of different names as the input. Your code should work for any name. Your code should only output the number,
# no other text is needed.
#
# Hint
# Remember, you can use len() around any piece of text to calculate the number of characters.
#
# e.g. https://www.google.com/search?q=how+to+get+the+length+of+a+string+in+python+stack+overflow
#
# Important
# Don't add prompt text to the input() function.
#
# e.g. use
#
# ✅ name = input()
#
# don't use:
#
# ❌ name = input("What's your name?")

# Inputs
# Mujeeb
# James
# Phillips
# Ernest Hemingway

print(len(input()))
