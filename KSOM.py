import sys

import numpy
import numpy as np


class KSOM:
    def __init__(self, h, w, num_of_clusters=100, alpha=0.6, r=0):
        self.learning_rate = alpha
        self.num_of_clusters = num_of_clusters
        # maybe change to tuple once we do part 1.2
        # uniform distribution for the weights
        if h==1:
            temp_clusters = np.random.rand((w, 2))
            self.clusters = [(i[0],i[1]) for i in temp_clusters]
        else:
            temp_clusters = np.random.rand((w, 2))
            Temp_clusters = [(i[0],i[1]) for i in temp_clusters]
            k =0
            for i in range(10):
                for j in range(10):
                    self.clusters[i][j] = Temp_clusters[k]
                    k+=1
        self.shape = (h,w)
        self.radius = r

    def fit(self, input_data, num_of_iterations):
        for t in num_of_iterations:
            # check if we need to make the points random
            for point in input_data:
                # parameters to hold info from the following loop
                best_Dj = sys.maxsize
                best_j = 0
                # run on all clusters
                for j in range(self.num_of_clusters):
                    # dj for x   =  w_ij   -  x
                    d_j_x = (self.clusters[j][0] - point[0])
                    d_j_y = (self.clusters[j][1] - point[1])
                    D_j = d_j_x ** 2 + d_j_y ** 2
                    if best_Dj > D_j:
                        best_Dj = D_j
                        best_j = j
                self.update_weights(best_j, point, t)
            self.update_learning_rate(t)
            self.update_radius(t)

    def update_weights(self, best_j, current_point, t):
        print("yuvi needs to write this code")

    def update_learning_rate(self, t):
        # lessen the learning rate
        self.learning_rate = 0.9 * (1 - (t / 1000))
        pass

    def update_radius(self, t):
        # update the radius
        pass
