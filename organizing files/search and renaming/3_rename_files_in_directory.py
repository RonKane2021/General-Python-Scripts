import os
  
# Function to rename multiple files
#source https://www.geeksforgeeks.org/rename-multiple-files-using-python/

dest = "C:\\test\\"


for count, filename in enumerate(os.listdir(dest)):
    dst = "PDF" + str(count) + ".pdf"
    src = dest + filename
    dst = dest + dst
          
        # rename() function will
        # rename all the files
    os.rename(src, dst)

print ("Finished Renaming Files")