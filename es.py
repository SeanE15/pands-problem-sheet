# this is a program that will read in a text file - and output the number of times 'e' appears in the file 
#Author: Sean Elliott 

# Download link for moby dick.txt https://gist.github.com/StevenClontz/4445774 
# https://stackoverflow.com/questions/37400974/unicode-error-unicodeescape-codec-cant-decode-bytes-in-position-2-3-trunca
# https://realpython.com/python-command-line-arguments/
# https://pythonexamples.org/python-count-occurrences-of-word-in-text-file/
# https://pythonexamples.org/python-count-number-of-characters-in-text-file/

#filename = 'C:\Users\Sean\Desktop\programming\mobydick.txt'
#with open (filename, 'rt') as f: 
    #read_data = f.read() 
    #print(read_data) 

filename = input("Enter a filename: ")
with open(filename) as f:
    next(f)
    for lines in f:
        open(r"C:\Users\Sean\Desktop\mobydick.txt", "rt")
        data = file.read()
        number= data.count("e")
        print ('Number of e in text file: ', number)



