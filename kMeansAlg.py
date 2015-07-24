__author__ = 'karic_000'
import random
import csv


def start():

    csv_file = open('simple-soccer-database.csv', 'rt')

    try:
        reader = csv.reader(csv_file)
        next(reader)    # Skip headers.
        stats = [[int(item) for number, item in enumerate(row) if
                item and (1 <= number <= 100)] for row in reader]
                # Converts list of strings into integers
        """The maximum number of rows for this program is 100"""
        print("\nDATA RETRIEVED:\n", stats)

        row_amount = len(stats)
        print("\nROW AMOUNT:",row_amount)
        col_amount = 11
        print("\nThe number of columns were -decided- to be static; so 11 it is.\n")
        dimensions = row_amount * col_amount  # The amount of elemets in the data.
        print('\nThe number of total elements:', dimensions)

        # clusters = [[] for i in range(4)]    # Creates 5 empty clusters
        cluster_1 = []
        cluster_2 = []
        cluster_3 = []
        cluster_4 = []
        cluster_5 = []

        cluster_list_size = row_amount//5  # Defines how many rows from "stats" can each cluster have.
        print("\nEach cluster should have this many rows put into them:", cluster_list_size)

        index = 0
        for i in range(0,5):   # There are 5 clusters .: Loop through them from 0-4
            observation = stats[index]
            print("\nObservation:", observation)
            x = random.randint(0,4)   # Random cluster takes the next observation
            print("Cluster's index:", x)
            #cluster_pick()
            if x == 0:
                cluster_1.append(observation)
            if x == 1:
                cluster_2.append(observation)
            if x == 0:
                cluster_3.append(observation)
            if x == 1:
                cluster_4.append(observation)
            if x == 0:
                cluster_5.append(observation)
                # if len(clusters) <= :    # If cluster is full
                print("\nNewly changed cluster:")
                print(cluster_1, cluster_2, cluster_3, cluster_4, cluster_5)
                index += 1  # To loop through every row (list in cluster)
        print(cluster_1, cluster_2, cluster_3, cluster_4, cluster_5)

#def cluster_pick(x):
    #if x == 0:
        #cluster = cluster_one

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

start()


