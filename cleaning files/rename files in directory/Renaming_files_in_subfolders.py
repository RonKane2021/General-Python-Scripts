#https://stackoverflow.com/questions/38948774/python-append-folder-name-to-filenames-in-all-sub-folders

import os

directory = "C:\\Test\\"

for root, dirs, files in os.walk(directory):
    if not files:
        continue
    prefix = os.path.basename(root)
    for f in files:
        os.rename(os.path.join(root, f), os.path.join(root, "{}_{}".format(prefix, f)))
        
print ("Finished")