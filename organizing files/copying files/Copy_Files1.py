
source1 = "C:\\test1\\*" #leave the * as a wildcard.  This will scan all the folders.
dest1 = "C:\test2\\" #Output Folder

import glob, os, shutil

print ("Starting")
print (" ")

files = glob.iglob(os.path.join(source1, "*.txt")) #Change the type of extention file here.
for file in files:
    if os.path.isfile(file):
        shutil.copy2(file, dest1)

    
        
print ("Copying Files is complete")
