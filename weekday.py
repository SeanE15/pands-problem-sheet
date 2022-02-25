# Write a program that outputs whether or not today is a weekday.
# Author: Sean Elliott 


# I start by using the built in module "datetime" which will display the current day of the week. I ask python to import this info for the current day/time.
import datetime 
x = datetime.datetime.now()

# I then set the parameters for the definition of weekday and weekend. This will then allow me to create a if/else selection which is crude but works exactly as I want it to.
weekDay = ("Monday",
        "Tuesday",
        "Wednesday", 
        "Thursday", 
        "Friday",)

weekEnd = ("Saturday", 
        "Sunday")

# I then specify that if x = a weekday (as defined by the list above) it will print out one statement; if not it will print out the other statement.
if x == weekDay: 
    print ("Yes, today is unfortunately a weekday...!")
else:
    print ("It is the weekend, yay!") 

# I will look to find out some way of tidying the inputs (weekDay and weekEnd) to see if they can be made to look even shorter.
