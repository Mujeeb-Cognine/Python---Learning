# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

# The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person
# both weigh the same amount, the short person is usually more overweight.
#
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

# Example Input 1
# 1.75
# 80
# means: weight = 80 and height = 1.7


# Write your code below this line 👇
# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
weight_as_int = int(weight)

height_as_int = float(height)

# Using the operator **
BMI = weight_as_int / height_as_int ** 2

# Using multiplication and PEMDAS
BMI = weight_as_int / (height_as_int * height_as_int)

bmi_as_int = int(BMI)
print(bmi_as_int)
