#This program looks for specific word in text files and replaces them with any word or phrases.

import os, re, shutil

inpath = "C:\\test2\\"
outpath= "C:\\test3\\"

word = "hello"

print ("Removing the following words that appear first: ", word, "\n")

for filename in os.listdir(inpath): #this is a loop in python
    filein = open(inpath + filename, 'r')
    fileout = open(outpath + filename, 'w')
    filedata = filein.read()
    filein.close()
    w1 = re.search(word, filedata, re.IGNORECASE)
    if w1 == None:
        pass
    else:
        new = filedata.replace(word, "world") #put new word here
        fileout.write(new)

fileout.close()

print ("Finish")

    
        

