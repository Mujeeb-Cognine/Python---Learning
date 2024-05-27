print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
# = is a assignment
# == is to check equality
if height >= 120:
    print("You can ride the rollercoaster!")
    if age < 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you have to grow taller before you can ride.")

# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#
# It should tell them the interpretation of their BMI based on the BMI value.
#
# Under 18.5 they are underweight
# Equal to or over 18.5 but below 25 they have a normal weight
# Equal to or over 25 but below 30 they are slightly overweight
# Equal to or over 30 but below 35 they are obese
# Equal to or over 35 they are clinically obese.

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Example Input 1
# 1.50
# 63
# Example Output 1
# Your BMI is 28.0, you are slightly overweight.
# since 63 ÷ (1.50 x 1.50) = 28
#
# The testing code will check for print output that is formatted like one of the lines below:
#
# "Your BMI is 18.28678, you are underweight."
# "Your BMI is 22.0, you have a normal weight."
# "Your BMI is 28.50752, you are slightly overweight."
# "Your BMI is 32.56189, you are obese."
# "Your BMI is 37.50000, you are clinically obese."
# Example Input 2
# 1.60
# 96
# Example Output 2
# Your BMI is 37.49999999999999, you are clinically obese.
# Example Input 3
# 1.71
# 73
# Example Output 3
# Your BMI is 24.96494647925858, you have a normal weight.


height = float(input())  # in meters e.g., 1.55
weight = int(input())  # in kilograms e.g., 72
# Your code below this line 👇
bmi = weight / (height * height)
if bmi < 18.5:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice.
#
# This is how you work out whether if a particular year is a leap year.
#
# on every year that is divisible by 4 with no remainder
#
# except every year that is evenly divisible by 100 with no remainder
#
# unless the year is also divisible by 400 with no remainder
#
# If english is not your first language or if the above logic is confusing, try using this flow chart .
#
# e.g. The year 2000:
#
# 2000 ÷ 4 = 500 (Leap)
#
# 2000 ÷ 100 = 20 (Not Leap)
#
# 2000 ÷ 400 = 5 (Leap!)
#
# So the year 2000 is a leap year.
#
# But the year 2100 is not a leap year because:
#
# 2100 ÷ 4 = 525 (Leap)
#
# 2100 ÷ 100 = 21 (Not Leap)
#
# 2100 ÷ 400 = 5.25 (Not Leap)
#
# Warning your output should match the Example Output format exactly, including spelling an punctuation.
#
# Example Input 1
# 2400
# Example Output 1
# Leap year
# Example Input 2
# 1989
# Example Output 2
# Not leap year


# Which year do you want to check?
year = int(input())
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
if year % 4 == 0:
    if (year * 2) % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")
