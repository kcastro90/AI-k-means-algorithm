__author__ = 'karic_000'
import random
import csv

csv_file = open('simple-soccer-database.csv', 'rt')
elements = []
stats = []

try:
    reader = csv.reader(csv_file)
    next(reader)    # Skip headers.
    ints = [[int(item) for number, item in enumerate(row) if item and (1 <= number <=12)] for row in reader]
    print(ints)
    
    print("\n THIS WILL BE THE OUTPUT WITHOUT INCLUDING THE FIRST COLUMN:\n")
    for col in reader:
        print(col[1::])
        # omit first COLUMN
        elements.append(col[1::])   # THIS WILL BE THE ARRAY OF ELEMENTS (including column label)

    print("\n THIS WILL BE THE DATA TO BE USED (it excludes the 12 column labels):\n")
    stats = elements[1::]
    print(stats)

    rowAmount = len(stats)
    colAmount = 11
    dimensions = rowAmount * colAmount  # 20 rows 11 columns in this example
    sums = stats[0][0] + stats[0][1]
    #print(sums)
    cluster = [[] for i in range(4)]    # Creates 5 empty clusters
    # clusters = [], [], [], [], []

    # ClusterListSize defines how many rows from "stats" can each cluster have
    clusterListSize = rowAmount//5
    print("\nEach cluster should have this many rows:")
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


    #MAKE STRINGS INTO INTEGERS

    """def centroids(lst)
    mean = sum(lst) / n
    return mean"""


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




