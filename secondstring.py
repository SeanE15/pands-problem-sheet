# This is a program that asks the user to input a string 
# and outputs every second letter in reverse order.
# Author: Sean Elliott 


# We start by asking the user to input a sentence
question = input('Please enter a sentence: ')

# we then must calculate the length of the string so that we can then start slicing; this specific line asks python to determine
# the length of the inputted sentence.
stringLength=len(question) 

# we then take the length of the string (sentence) and ask it to only output every second character while also reversing the sentence. This works by starting with the length 
# of the string and ending at index 0.

slicedString=question[stringLength::-2]

# we then get the program to print ou the sliced sentence.
print (slicedString) 