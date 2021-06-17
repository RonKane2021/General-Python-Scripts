import os

source = "C:\\" # This will scan all the folders.

a = open('test.txt', 'w')

backspace = "\\" 
space = "\n" 

print("Starting and searching for files")
print(" ")

"""
Will go through the directory and find all the files with the 
extention. For this example it will look for pdfs. If the file extension
is found then it will write the locaton on a text file.

"""

for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith('.pdf'):
            a.write(root)
            a.write(backspace)
            a.write(file)
            a.write(space)
a.close()   
        
print ("Searching for files is complete")