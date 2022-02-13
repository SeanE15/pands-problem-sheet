# This is a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two,
# but if it is odd, multiply it by three and add one. The program must end at value of 1.
# Author: Sean Elliott 

number = int(input(" Please enter a positive integer: ")) 

# We ask the user to input an integer, and then outline the below parameters for the code to analyse whether it is even or odd.
if (number % 2) == 0:
# Double brackets helped me to compartmentalise what part of the process was happening first. We then must ask python to divide the even integer by 2 as per the insturctions.
# I used 2 // signs to bring the number to it's most basic value (ie. no decimal places)
    print((number) // 2)
# If the program finds that the integer is odd we ask python to multiply the answer by 3 and add 1. Again double brackets help to outline which parts
# of the process are happening first and also help when we are changing the number "1" to an integer (as it will not work as a string).
else:
    print((number * 3) + int(1)) 
# We now must get the program to continue processing these following numbers until It hits the number 1. The program should then stop.
while number >= 1: 
     print (number) 
