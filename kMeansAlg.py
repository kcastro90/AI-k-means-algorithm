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

        cluster_1, cluster_2, cluster_3, cluster_4, cluster_5 = [], [], [], [], []

        cluster_list_size = row_amount//5  # Defines how many rows from "stats" can each cluster have.
        print("\nEach cluster should have this many rows put into them:", cluster_list_size)

        done = False
        index = 0
        while not done:
            if index <= row_amount: # 0 - 20 in this example
                print("\nRow index:", index)
                observation = stats[index]
                print("Observation:", observation)
                x = random.randint(0,4)   # Random cluster takes the next observation
                # print("Cluster's index:", x)
                # 5 Clusters options.
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
                if index == 19:
                    done = True
                if index <= 18:
                    index += 1  # To loop through every row (list in cluster)
        print("\nCluster 1:", cluster_1)
        print("\nCluster 2:", cluster_2)
        print("\nCluster 3:", cluster_3)
        print("\nCluster 4:", cluster_4)
        print("\nCluster 5:", cluster_5)

    finally:
        csv_file.close()

start()


