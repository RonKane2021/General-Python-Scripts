import shutil

dest = "C:\\test\\" #Output Folder

print ("Starting to copy files")

"""
Will go through the text file from 1_searching_for_file.py script
and copy all the files that were found and dump them into the output folder.
If any error occurs we will pass using the Exception class.
"""

b = open('test.txt', 'r')
for line in b:
    c = line.strip("\n")
    try:
        shutil.copy(c, dest)
    except Exception:
        print ("Some file couldn't be transfered!")
        pass
                
b.close()
                
print ("Copying Files is complete")