# Write a program that takes a positive floating-point number as input and outputs an approximation of its square root.
# You should create a function called <tt>sqrt</tt> that does this.
# Author: Sean Elliott 


sqrt = []

def sqrt(number):   
    a = float(number)
    for a in range(number): 
        number = 0.5 * (number + a/number) 
        print (number)

a = int(input("Enter a positive integer:"))
#print("The square root of {} is approximately {}") 
print(sqrt)

#input("Please enter a positive number: ") 
#answer = sqrt
#print ("The square root of {} is approximately {}") 