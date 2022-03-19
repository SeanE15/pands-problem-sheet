# This is a program that asks the user to input any positive integer
# and outputs the successive values of the following calculation.
# At each step calculate the next value by taking the current value and, if it is even, divide it by two,
# but if it is odd, multiply it by three and add one. The program must end at value of 1.
# Author: Sean Elliott 

def collatz(number): 

# We start by defining the function of 'collatz' which is a built in function in Python.
    if (number % 2) == 0:
# Double brackets helped me to compartmentalise what part of the process was happening first. We then must ask python to divide the even integer by 2 as per the insturctions.
# I used 2 // signs to bring the number to it's most basic value (ie. no decimal places) If the number is even, the program will return an even answer.
        print((number) // 2)
        return number // 2
# If the program finds that the integer is odd we ask the program to multiply the answer by 3 and add 1. Again double brackets help to outline which parts
# of the process are happening first. We then ask the  program to return the value that it has calculated (so that the answer is displayed).
    elif (number % 2) == 1:
        answer = ((number * 3) + 1)
        print(answer)
        return (answer)
# The above is the program that we will be running below, the intial stages are all outlining how we want the program to perform.
# We now must get the program to continue processing these following numbers until it hits the number 1. The program should then stop.
# We use a while loop to break the chain while the integer is not equal to 1. Once 1 is reached, the program ends.

number = (input(" Please enter a positive integer: ")) 
while number != 1:
    number = collatz(int(number))
