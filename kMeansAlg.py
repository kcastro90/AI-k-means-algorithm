__author__ = 'karic_000'

import random
import csv

#import sys

csvfile = open('simple-soccer-database.csv', 'rt')

#Create 5 clusters
cluster1 = []
cluster2 = []
cluster3 = []
cluster4 = []
cluster5 = []
elements = []
try:
    reader = csv.reader(csvfile)
    for col in reader:
        #12 columns and 21 rows
        #omit first row
        elements.append(col[1:12])
    #print (elements)
    #11*21 = 231 elements
    stats = elements[11:230]
    print (stats)


finally:
    csvfile.close()
