__author__ = 'karic_000'
import random
import csv


def initialization():

    csv_file = open('simple-soccer-database.csv', 'rt')

    try:
        reader = csv.reader(csv_file)
        next(reader)    # Skip headers.
        stats = [[int(item) for number, item in enumerate(row) if item and (1 <= number <= 100)] 
                 for row in reader]   # Converts string into int
        """The maximum number of rows for this program is 100"""
        print("\nDATA RETRIEVED:\n", stats)

        row_amount = len(stats)
        print("\nROW AMOUNT:", row_amount)
        col_amount = 11
        print("\nThe number of columns were -decided- to be static; so 11 it is.")
        dimensions = row_amount * col_amount  # The amount of elements in the data.
        print('\nThe number of total elements:', dimensions)
        assignment_step(stats, row_amount)
    finally:
        csv_file.close()


def assignment_step(stats, row_amount):
        cluster_1, cluster_2, cluster_3, cluster_4, cluster_5 = [], [], [], [], []
        clusters = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5]

        cluster_list_size = row_amount//5  # Defines how many rows can each cluster have.
        print("\nEach cluster should have this many rows put into them:", cluster_list_size)

        done = False
        index = 0
        while not done:
            if index <= row_amount:  # 0 - 20 in this example
                observation = stats[index]
                x = random.randint(0, 4)   # Random cluster takes the next observation
                if index < row_amount:  # When index hits the last item 19,
                    # it increments til 20, but doesn't include it, then it halts
                    # 5 Clusters options.
                    if x == 0:
                        if len(cluster_1) < cluster_list_size:
                            cluster_1.append(observation)
                            # Only increments if that row is used
                            index += 1
                        else:
                            # Pick a new random cluster
                            x = random.randint(1, 4)
                    if x == 1:
                        if len(cluster_2) < cluster_list_size:
                            cluster_2.append(observation)
                            index += 1
                        else:
                            x = random.randint(0, 4)
                    if x == 2:
                        if len(cluster_3) < cluster_list_size:
                            cluster_3.append(observation)
                            index += 1
                        else:
                            x = random.randint(0, 4)
                    if x == 3:
                        if len(cluster_4) < cluster_list_size:
                            cluster_4.append(observation)
                            index += 1
                        else:
                            x = random.randint(0, 4)
                    if x == 4:
                        if len(cluster_5) < cluster_list_size:
                            cluster_5.append(observation)
                            index += 1

                if index == row_amount:
                    done = True
        print("\nCluster 1:", cluster_1, "\nCluster 2:", cluster_2, "\nCluster 3:", cluster_3,
              "\nCluster 4:", cluster_4, "\nCluster 5:", cluster_5)

        """
        empty_cluster_index = ""
        count = 0
        full = False
        for cluster in clusters:
            if cluster == 0:
                empty_cluster_index = count
            else:
                count += 1
            print(empty_cluster_index)"""

        update_centroids(cluster_1, cluster_2, cluster_3, cluster_4, cluster_5)


def update_centroids(c_1, c_2, c_3, c_4, c_5):
    centroid_1cluster, centroid_2cluster, centroid_3cluster, centroid_4cluster, \
        centroid_5cluster = [], [], [], [], []
    index = 0

    # Makes sure no cluster is empty before beginning the update step.
    if len(c_1) or len(c_2) or len(c_3) or len(c_4) or len(c_5) != 0:
        # Check if any of the clusters are empty.
        # print("Length for each cluster:",len(c_1), len(c_2), len(c_3), len(c_4), len(c_5))

        while index < len(c_1):
            centroid = [sum(c_1[index])/(len(c_1[0]))]
            centroid_1cluster.append(centroid)
            index += 1
        index = 0
        print("\nThe centroids for Cluster 1:", centroid_1cluster)
        while index < len(c_2):
            centroid = [sum(c_2[index])/(len(c_2[0]))]
            centroid_2cluster.append(centroid)
            index += 1
        index = 0   # Reset index to 0
        print("The centroids for Cluster 2:", centroid_2cluster)
        while index < len(c_3):
            centroid = [sum(c_3[index])/(len(c_3[0]))]
            centroid_3cluster.append(centroid)
            index += 1
        index = 0   # Reset index to 0
        print("The centroids for Cluster 3:", centroid_3cluster)
        while index < len(c_4):
            centroid = [sum(c_4[index])/(len(c_4[0]))]
            centroid_4cluster.append(centroid)
            index += 1
        index = 0   # Reset index to 0
        print("The centroids for Cluster 4:", centroid_4cluster)
        while index < len(c_5):
            centroid = [sum(c_5[index])/(len(c_5[0]))]
            centroid_5cluster.append(centroid)
            index += 1
        index = 0   # Reset index to 0
        print("The centroids for Cluster 5:", centroid_5cluster)


initialization()

