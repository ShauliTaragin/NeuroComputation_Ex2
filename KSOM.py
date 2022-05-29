import numpy
import numpy as np


class KSOM:
    def __init__(self, num_of_clusters = (2,100), alpha = 0.6 , r = 0):
        self.learning_rate = alpha
        self.num_of_clusters = num_of_clusters
        # maybe change to tuple once we do part 1.2
        # uniform distribution for the weights
        self.clusters = np.random.rand(num_of_clusters)
        self.radius = r


    def fit(self , input_data , num_of_iterations):
        for t in num_of_iterations:


