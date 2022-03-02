# Write a program that outputs whether or not today is a weekday.
# Author: Sean Elliott 


# I start by using the built in module "datetime" which will display the current day of the week. I ask python to import this info for the current day/time and then use the weekday. 
# function to assign a number a number to each weekday starting at 0 for Monday. We will then get the program to distinguish what day of the week it is based on this reading.
import datetime 
x = datetime.datetime.today().weekday()

# Python arranges the days of the week as a set of integers. The program will then follow the instructions below and print out
# the correct print out based on whether it is a weekday/weekend. 0-4 are week days and 5/6 are Sat/Sun.

if x <= 5: 
    print("Yes, today is unfortunately a weekday...!")
else: 
    print("It is the weekend, yay!") 

# if 'x' (the current day) is a weekday (as defined by the list above) it will print out the weekday statement; if not it will print out the other .

