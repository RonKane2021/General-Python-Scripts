""" This quick script will reduce the amount data points in a csv file down 
using the islide function. Sometimes csv files contain massive amounts of data
or time points that are often easier when reduced.
"""

import csv
from itertools import islice

original = "C:\\test\\HPLC.csv" #Input csv file
reduced = "C:\\test\\out.csv" #Output csv file


with open(original) as f, open(reduced,"w") as out:
        r = islice(f, 0 ,None, 20)
        out.writelines(r)
f.close
out.close
print ("finished")