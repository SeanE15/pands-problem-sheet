
# This is a program that calculates Body Mass Index (BMI)
# Author: Sean Elliott

# First we will get the information from the user and convert those strings to float functions (for the decimal place numbers).

Weight = float(input("Please enter your weight in kg: "))

Height = float(input("Please enter your height in cm: "))

# We must then calcutate the BMI by converting the height and weight into common numbers. I do this by converting the height from centimeter to meters (dividing by 100) and then dividng the weight into the height.

BMI = Weight / (Height/100)**2

# Now we must print the answer for the user to give them their BMI reading. 

print (f"Your BMI is {BMI}")