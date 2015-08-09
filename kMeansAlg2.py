""" This will read a csv file of any column and row length"""
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
        dimensions = 0  # The amount of elements in the data.
        for row in stats:
            for col in row:
                dimensions += 1
        print('\nThe number of total elements:', dimensions)
        col_amount = dimensions // row_amount
        print("\nCOLUMN AMOUNT:", col_amount)

        # Create 5 clusters and assign to each the same amount of elements from the data
        cluster_1, cluster_2, cluster_3, cluster_4, cluster_5 = [], [], [], [], []
        clusters = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5]

        cluster_list_size = row_amount//len(clusters)  # Defines how many rows can clusters hold
        print("\nEach cluster should have this many rows put into them:", cluster_list_size)

        assignment_step(stats, row_amount, col_amount, cluster_1, cluster_2, cluster_3, cluster_4,
                        cluster_5, cluster_list_size, clusters)

    finally:
        csv_file.close()


def assignment_step(stats, row_amount,col_amount, cluster_1, cluster_2, cluster_3, cluster_4,
                    cluster_5, cluster_list_size, clusters):

        done = False
        index = 0
        while not done:
            if index <= row_amount:  # 0 - 20 in this example
                observation = stats[index]
                x = random.randint(0, 4)   # Random cluster takes the next observation
                if index < row_amount:  # When index hits one before the last row
                    # it increments again, adds it to cluster, then it halts
                    if x == 0:  # x identifies which of the 5 clusters was chosen
                        if len(cluster_1) < cluster_list_size:  # Checks if cluster is full
                            cluster_1.append(observation)
                            # Only increments if that row is used
                            index += 1
                        else:
                            # Cluster is full, pick a new random cluster
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

        clust_index = 0 # Keeps rr
        sums = 0
        ind_i = 0  # every Nth element in a cluster's columns
        next_r = 0  # to keep the row number; 4 max
        limit = 0  # Keep track of "dimensions"
        cluster_dimension = cluster_list_size * col_amount  # 44 elements
        centroid_1, centroid_2, centroid_3, centroid_4, centroid_5 = [], [], [], [], []
        centroids = centroid_1, centroid_2, centroid_3, centroid_4, centroid_5
        for each in centroids:
            #cent1 = []
            which_clust = clusters[clust_index]
            which_centroid = centroids[clust_index]
            for r in which_clust:
                for c in r:
                    while next_r < cluster_list_size: # Cluster size is 4 in this example
                        sums += which_clust[next_r][ind_i]
                        next_r += 1
                        limit += 1

                    if next_r == cluster_list_size and limit != cluster_dimension:
                    # limit's max will always be 1 less than cluster_dimensions
                        centroid = sums/cluster_dimension
                        which_centroid.append(centroid)
                        sums = 0
                        next_r = 0  # Loop back through every "N"th elements .
                        ind_i += 1  # After very 4 checks, increase list index
            if next_r == cluster_list_size and limit == cluster_dimension:
                centroid = sums/cluster_dimension
                which_centroid.append(centroid)
            limit = 0
            ind_i, next_r = 0, 0
            clust_index += 1
        print("\nCentroid 1", centroid_1, "\nCentroid 2", centroid_2, "\nCentroid 3", centroid_3,
              "\nCentroid 4", centroid_4, "\nCentroid 5", centroid_5,)

        cluster_1trans = [list(a) for a in zip(*cluster_1)]
        cluster_2trans = [list(a) for a in zip(*cluster_2)]
        cluster_3trans = [list(a) for a in zip(*cluster_3)]
        cluster_4trans = [list(a) for a in zip(*cluster_4)]
        cluster_5trans = [list(a) for a in zip(*cluster_5)]

        print("\nLIST OF EACH CLUSTER'S COLUMNS\nCluster 1:", cluster_1trans, "\nCluster 2:",
              cluster_2trans, "\nCluster 3:", cluster_3trans, "\nCluster 4:", cluster_4trans,
              "\nCluster 5:", cluster_5trans)
        #done = False
        #iteration = 0
        # Will keep track of the cluster in "clusters" index
        # It will also be the clusters' index that needs an element
        """while done:
            for cluster in clusters:    # Search to see if any cluster was left empty

                    # Cluster that is losing a row
                    iteration += 1  # There are only 5 clusters so it won't go beyond scope
                done = True"""
        """print("\nIf any clusters were updated, this print will show their modifications:\n\n"
              "Cluster 1:", cluster_1, "\nCluster 2:", cluster_2, "\nCluster 3:",
              cluster_3, "\nCluster 4:", cluster_4, "\nCluster 5:", cluster_5)"""



        """while index < len(c_4):
            centroid = [sum(c_4[index])/(len(c_4[0]))]
            centroid_4cluster.append(centroid)
            index += 1"""

initialization()
