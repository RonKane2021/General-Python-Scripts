#This program looks for word in a directory of text files. If the word is found then it gets copied to the outpath folder.

import os, re, shutil

inpath = "C:\\test\\"
outpath= "C:\\test2\\"

word = "hello"

print ("Searching the files with the following word: ", word, "\n")

for filename in os.listdir(inpath): #this is a loop in python
    filein = open(inpath + filename, 'r')
    filedata = filein.read()
    w1 = re.search(word, filedata, re.IGNORECASE)
    if w1 == None:
        pass
    else:
       shutil.copy(inpath + filename,outpath)
            
    filein.close()

print ("Finish")

    
        

