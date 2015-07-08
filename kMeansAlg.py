__author__ = 'karic_000'

import csv
import sys

csvfile = open('simple-soccer-database.csv', 'rt')
try:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
finally:
    csvfile.close()
