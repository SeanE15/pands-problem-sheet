# This is a program that will read in a text file - and output the number of times 'e' appears in the file 
#Author: Sean Elliott 

def letterCount(fileName, letter):
# We start by defining the function 'letterCount' which will read in two values for later in the program
 
    file = open(fileName, "r")
# I start by asking the program to open the file, and open it in the read format only. This is denoted by the 'r'.

    text = file.read()
# I ask the program to read the entire text file - note that we have not asked it to output the file - only scan it for the information that we require.

    return text.count(letter)
# I have now asked the program to perform the count function which will count the entire txt doc and calculate the number of letters designated by the below line of code. 
# Please note that the 'e' is in fact case sensitive and as such it is not counting capital E's.

print(letterCount(r'pands-problem-sheet\pands-problem-sheet\mobydick.txt', 'e'))
# The program will now print out the result - note that I have designated the file location above - and also the exact letter (which in this case is the 'e') which I want to be counted.
# The 'r' infront of the file path above was used because my file path was a normal string - which was throwing an error. Using the r before the normal string has converted it into a raw string.
# The program will now count the letter 'e' form the file that I have attached in the pands-problem-sheet repository rather than from my own computer - meaning that the program can be download
# and used by anyone who downloads the program from Github.