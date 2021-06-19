""" This program looks for words in text files. The files with any strings will be 
copied to the dest folder and if no words are found then the file is displayed
on the python shell
"""

import os, re, sys, shutil

inpath = "C:\\test\\"
dest = "C:\\test2\\"


print ("These files do not have any words in their document!")
print ()

for filename in os.listdir(inpath): #this is a loop in python
    filein = open(inpath + filename, 'r')
    stringlength = filein.read()
    if len(stringlength) > 1:
        shutil.copy(inpath + filename,dest)
    else:
        print (filename, '\n')
    filein.close()

    
        

