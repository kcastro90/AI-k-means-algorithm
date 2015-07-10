__author__ = 'karic_000'
import random
import csv

#import sys

csvfile = open('simple-soccer-database.csv', 'rt')
elements = []
stats = []

try:
    reader = csv.reader(csvfile)
    print ("\n THIS WILL BE THE OUTPUT WITHOUT INCLUDING THE FIRST COLUMN:\n")
    for col in reader:
        print (col[1::])
        #omit first COLUMN
        elements.append(col[1::])

    print ("\n THIS WILL BE THE NEW ARRAY OF ELEMENTS (including column label):\n")
    print (elements)

    print ("\n THIS WILL BE THE DATA TB BE USED (it excludes the 12 column labels):\n")
    stats = elements[11::]
    print (stats)
    
        #(random.choice(stats))  # Choose a random element
finally:
    csvfile.close()

  

