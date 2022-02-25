# Write a program that outputs whether or not today is a weekday.
# Author: Sean Elliott 

import datetime 
x = datetime.datetime.now()

weekDay = ("Monday",
        "Tuesday",
        "Wednesday", 
        "Thursday", 
        "Friday",)

weekEnd = ("Saturday", 
        "Sunday")

if x == weekDay:
    print ("Yes, today is unforutnately a weekday...!")
else:
    print ("It is the weekend, yay!") 

