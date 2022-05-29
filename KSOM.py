import sys

import numpy
import numpy as np


class KSOM:
    def __init__(self, num_of_clusters=(2, 100), alpha=0.6, r=0):
        self.learning_rate = alpha
        self.num_of_clusters = num_of_clusters
        # maybe change to tuple once we do part 1.2
        # uniform distribution for the weights
        self.clusters = np.random.rand(num_of_clusters)
        self.radius = r

    def fit(self, input_data, num_of_iterations):
        for t in num_of_iterations:
            # check if we need to make the points random
            for point in input_data:
                # parameters to hold info from the following loop
                best_Dj = sys.maxsize
                best_j = 0
                # run on all clusters
                for j in range(self.num_of_clusters[1]):
                    # dj for x   =  w_ij   -  x
                    d_j_x = (self.clusters[0][j] - point[0])
                    d_j_y = (self.clusters[1][j] - point[1])
                    D_j = d_j_x ** 2 + d_j_y ** 2
                    if best_Dj > D_j:
                        best_Dj = D_j
                        best_j = j
                self.update_weights(best_j, point,t)

    def update_weights(self , best_j,current_point,t):
