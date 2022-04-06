# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# Author: Sean Elliott 


# We start writing this program by creating a function called 'sqrt' as per the instructions. In the function below we create an if/else statement. 
# If the input is is less than 0 (ie. not a positive number) it will return a value fo zero. 
# If the number is greater than 0, the program will multiply the input by .5 to find the square root of the number.


def sqrt(a):   
    if a < 0:
        return 0
    else:
        return (a ** 0.5)

a = int(input("Enter a positive integer:"))

print(sqrt(a))
