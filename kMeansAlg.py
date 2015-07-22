__author__ = 'karic_000'
import random
import csv
#import numpy as np

csv_file = open('simple-soccer-database.csv', 'rt')
elements = []
stats = []

try:
    reader = csv.reader(csv_file)
    print("\n THIS WILL BE THE OUTPUT WITHOUT INCLUDING THE FIRST COLUMN:\n")
    for col in reader:
        print(col[1::])
        # omit first COLUMN
        elements.append(col[1::])

    print("\n THIS WILL BE THE ARRAY OF ELEMENTS (including column label):\n")
    print(elements)

    print("\n THIS WILL BE THE DATA TB BE USED (it excludes the 12 column labels):\n")
    stats = elements[1::]
    print(stats)

    rowAmount = len(stats)
    colAmount = 11
    dimensions = rowAmount * colAmount  # 20 rows 11 columns in this example
    cluster = [[] for i in range(4)]    # Create 5 empty clusters

    # ClusterListSize defines how many rows from "stats" can each cluster have
    clusterListSize = rowAmount//5

    random_choice1 = random.sample(stats, clusterListSize)
    print(random_choice1)
    
    """NOW I'M TRYING TO ASSIGN A random_choice LIST OF ROWS TO EACH OF THE 5 CLUSTERS
    WITHOUT REPEATING ANY OF THE ROWS
    BEYOND THIS POINT IT'S ALL IRRELEVANT AT THIS STAGE"""

    
    # randOberservation = np.random.randint(dimensions, size=(rowAmount,colAmount))
    # Assign each observation/element to a random cluster
    # Loop over all observations
    """for observation in stats:
        clusterIndex = random.choice(clusters)
        # cluster = clusters[clusterIndex]
        # cluster.append(observation)
        clusters[clusterIndex].append(observation)
        print(clusters)"""

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




