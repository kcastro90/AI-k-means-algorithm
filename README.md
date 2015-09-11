# AI-k-means-algorithm
    This program reads a csv file (simple-soccer-database.csv), while ignoring all labels and only considering the numerical values to retrieve some statistics. 
Each row of elements are divided into five randomly arranged clusters, each containing the same amount of rows. 
    It was supposed to simulate an Random K-Means Algorithm. The rows/lists in each cluster is transposed so that each "nth" 
element, or column n of each row/list, can be grouped and have its centroid defined.
    This program has been implemented as far as to calculating the clusters' centroids, without an update step that updates
the clusters.
It is also able to find the minimum value for the first cluster and its index, which will eventually be removed and placed in 
another cluster with values closer to its own.
This program is not entirely finished.
