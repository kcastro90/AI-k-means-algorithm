__author__ = 'karic_000'
import random
import csv

csv_file = open('simple-soccer-database.csv', 'rt')
elements = []
stats = []

try:
    reader = csv.reader(csv_file)
    next(reader)    # Skip headers.
    stats = [[int(item) for number, item in enumerate(row) if
              item and (1 <= number <= 100)] for row in reader]
              # Converts list of strings into integers
    """The maximum number of rows for this program is 100"""
    print("\nDATA RETRIEVED:\n" )
    print(stats)

    rowAmount = len(stats)
    print("\nROW AMOUNT:")
    print(rowAmount)
    colAmount = 11
    print("\nThe number of columns were -decided- to be static; so 11 it is.\n")
    dimensions = rowAmount * colAmount  # 20 rows 11 columns in this example
    print('\nThe number of total elements:')
    print(dimensions)


    cluster = [[] for i in range(4)]    # Creates 5 empty clusters
    # clusters = [], [], [], [], []

    # ClusterListSize defines how many rows from "stats" can each cluster have
    clusterListSize = rowAmount//5
    print("\nEach cluster should have this many rows put into them:")
    print(clusterListSize)

    index = 0
    #for aRow in stats: # Go through each row in stat
        #for search_repeat in cluster[index]: # Search through all elements in that cluster

    random_row_index = random.randint(0,rowAmount)
    print("\nrandom_row_index:")
    print(random_row_index)
    cluster[index].append(random_row_index)
    del stats[random_row_index]
    print("\nnew stats:")
    print(stats)


    # def centroids(lst)
    # mean = sum(lst) / n
    # return mean"""


    # Assign each observation/element to a random cluster
    # Loop over all observations


    # done = False
    # while not done
        # sourceIndex = ranInt(K)
        # source = clusters[sourceIndex]
        # if (source not cluster && source.length > 1):
            # sourceObservationIndex = rndInt(source.length)
            # sourceObservation = source[sourceObservationIndex]
            # source.remove(sourceObservationIndex)
            # cluster.add(sourceObservation)
            # done = True
    # updateStep()


finally:
    csv_file.close()




