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
        """If columns were unknown, 2 nested for loops could have given that number"""
        dimensions = row_amount * col_amount  # The amount of elements in the data.
        print('\nThe number of total elements:', dimensions)

        # Create 5 clusters and assign to each the same amount of elements from the data
        cluster_1, cluster_2, cluster_3, cluster_4, cluster_5 = [], [], [], [], []
        clusters = [cluster_1, cluster_2, cluster_3, cluster_4, cluster_5]

        cluster_list_size = row_amount//5  # Defines how many rows can each cluster have.
        print("\nEach cluster should have this many rows put into them:", cluster_list_size)

        assignment_step(stats, row_amount, cluster_1, cluster_2, cluster_3, cluster_4, cluster_5,
                        cluster_list_size, clusters)

    finally:
        csv_file.close()


def assignment_step(stats, row_amount, cluster_1, cluster_2, cluster_3, cluster_4, cluster_5,
                    cluster_list_size, clusters):

        done = False
        index = 0
        while not done:
            if index <= row_amount:  # 0 - 20 in this example
                observation = stats[index]
                x = random.randint(0, 4)   # Random cluster takes the next observation
                if index < row_amount:  # When index hits one before the last row
                    # it increments again, adds it to cluster, then it halts
                    if x == 0:  # x indentifies which of the 5 clusters was chosen
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

        update_centroids(cluster_1, cluster_2, cluster_3, cluster_4, cluster_5)

        done = False
        iteration = 0
        # Will keep track of the cluster in "clusters" index
        # It will also be the clusters' index that needs an element

        while done:
            for cluster in clusters:    # Search to see if any cluster was left empty
                if len(cluster) == 0:   # If an empty one is found
                    print("iteration", iteration)
                    which_cluster = random.randint(0, 4)
                    print("Which cluster:", which_cluster)
                    # Randomly picks a new cluster index
                    giving_cluster = clusters[which_cluster]
                    print("Giving cluster:", giving_cluster)
                    # Checks if cluster that is going to give a row is not this empty one
                    if (cluster != giving_cluster) and (len(giving_cluster) > 1):
                        # Row index from cluster
                        index_for_row = random.randint(0, len(giving_cluster))
                        print("Which row index from cluster:", index_for_row)
                        new_row_elements = giving_cluster[index_for_row]  # Row that is being taken
                        print("New row's elements", new_row_elements)
                        # Find and assign clusters

                        # Cluster being added options
                        if iteration == 0:
                            cluster_1.append(new_row_elements)
                        if iteration == 1:
                            cluster_2.append(new_row_elements)
                        if iteration == 2:
                            cluster_3.append(new_row_elements)
                        if iteration == 3:
                            cluster_4.append(new_row_elements)
                        if iteration == 4:
                            cluster_5.append(new_row_elements)
                        print(cluster_1, cluster_2, cluster_3, cluster_4, cluster_5)

                        if which_cluster == 4:
                            cluster_1.remove(index_for_row)
                        if which_cluster == 1:
                            cluster_2.remove(index_for_row)
                        if which_cluster == 2:
                            cluster_3.remove(index_for_row)
                        if which_cluster == 3:
                            cluster_4.remove(index_for_row)
                        if which_cluster == 4:
                            cluster_5.remove(index_for_row)

                            """if which_cluster == 4:
                            del cluster_1[index_for_row]
                        if which_cluster == 1:
                            del cluster_2[index_for_row]
                        if which_cluster == 2:
                            del cluster_3[index_for_row]
                        if which_cluster == 3:
                            del cluster_4[index_for_row]
                        if which_cluster == 4:
                            del cluster_5[index_for_row]
                            THIS COULD WORK TOO."""
                    # Cluster that is losing a row
                    iteration += 1  # There are only 5 clusters so it won't go beyond scope
                done = True
        print("\nIf any clusters were updated, this print will show their modifications:\n\n"
              "Cluster 1:", cluster_1, "\nCluster 2:", cluster_2, "\nCluster 3:",
              cluster_3, "\nCluster 4:", cluster_4, "\nCluster 5:", cluster_5)

        # After no empty clusters are left update the centroids
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
        print("The centroids for Cluster 5:", centroid_5cluster)


initialization()
