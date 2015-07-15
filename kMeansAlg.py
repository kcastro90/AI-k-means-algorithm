__author__ = 'karic_000'
import random
import csv


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
    dimensions = rowAmount * 11
    # 20 rows 11 columns
    # print(stats[0][1]) 31

    # Create 5 clusters
    clusters = [[] for i in range(4)]

    # Assign each observation/element to a random cluster
    # Loop over all observations
    for observation in stats:
        clusterIndex = random.choice(clusters)
        cluster = clusters[clusterIndex]
        cluster.append(observation)
        print(clusters)

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




