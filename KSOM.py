import sys
import numpy as np
from matplotlib import pyplot as plt


class KSOM:
    def __init__(self, h, w, num_of_clusters=100, alpha=0.35, r=15):
        self.learning_rate = alpha
        self.num_of_clusters = num_of_clusters
        # maybe change to tuple once we do part 1.2
        # uniform distribution for the weights
        if h == 1:
            temp_clusters = np.random.rand(w, 2)
            self.clusters = [[[i[0], i[1]] for i in temp_clusters]]
        else:
            self.clusters = [[[0, 0]] * h for i in range(w)]
            for i in range(h):
                for j in range(w):
                    # since we have a 10x10 cluster matrix we want each point in the matrix to be in order
                    # therefore we draw x and y in this manner e.g i=0,j=0 ==> x=(0.0,0.1),y=(0.0,0.1)
                    x = np.random.uniform(i * (1 / h), i * (1 / h) + (1 / h))
                    y = np.random.uniform(j * (1 / w), j * (1 / w) + (1 / w))
                    self.clusters[i][j] = [x, y]
        self.shape = (h, w)
        self.radius = r

    def plotClusters(self, points, current_iteration, num_of_iteration):
        x_points = []
        y_points = []
        for i in range(len(points)):
            x_points.append(points[i][0])
            y_points.append(points[i][1])
        plt.scatter(x_points, y_points, alpha=0.3, color="navy")

        x_model_a = []
        y_model_a = []
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                x_model_a.append(self.clusters[i][j][0])
                y_model_a.append(self.clusters[i][j][1])
        plt.scatter(x_model_a, y_model_a, color="maroon")
        if self.shape[0] == 1:
            plt.plot(x_model_a, y_model_a, color="maroon")
        else:
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    if i - 1 >= 0:
                        plt.plot([self.clusters[i][j][0], self.clusters[i - 1][j][0]],
                                 [self.clusters[i][j][1], self.clusters[i - 1][j][1]], color="maroon")
                    if j - 1 >= 0:
                        plt.plot([self.clusters[i][j][0], self.clusters[i][j - 1][0]],
                                 [self.clusters[i][j][1], self.clusters[i][j - 1][1]], color="maroon")
                    if i + 1 < self.shape[0]:
                        plt.plot([self.clusters[i][j][0], self.clusters[i + 1][j][0]],
                                 [self.clusters[i][j][1], self.clusters[i + 1][j][1]], color="maroon")
                    if j + 1 < self.shape[1]:
                        plt.plot([self.clusters[i][j][0], self.clusters[i][j + 1][0]],
                                 [self.clusters[i][j][1], self.clusters[i][j + 1][1]], color="maroon")
        if current_iteration != num_of_iteration - 1:
            plt.title("Amount of Points:" + str(len(points)) + " | "
                      + "Num of Iter:" + str(num_of_iteration) +
                      "\n" +
                      "Current Iter:" + str(current_iteration) + " | " +
                      "Amount of Clusters:" + str(self.shape) + " | ")
        else:
            plt.title("Amount of Points:" + str(len(points)) + " | "
                      + "Num of Iter:" + str(num_of_iteration) +
                      "\n" +
                      "This is the final iteration" + " | " +
                      "Amount of Clusters:" + str(self.shape) + " | ")
        plt.xlim(0, 1)
        plt.ylim(0, 1)
        plt.show()

    def fit(self, input_data, num_of_iterations):
        for t in range(num_of_iterations):
            print(f"iter number :{t}")
            if t % 50 == 0 or t == 20:
                self.plotClusters(input_data, t, num_of_iterations)
            # check if we need to make the points random
            for point in input_data:
                # parameters to hold info from the following loop
                best_Dj = sys.maxsize
                best_j = 0
                # run on all clusters
                for i in range(self.shape[0]):
                    for j in range(self.shape[1]):
                        d_j_x = (self.clusters[i][j][0] - point[0])
                        d_j_y = (self.clusters[i][j][1] - point[1])
                        D_j = d_j_x ** 2 + d_j_y ** 2
                        if best_Dj > D_j:
                            best_Dj = D_j
                            best_j = [i, j]
                self.update_weights(best_j, point)
            self.update_learning_rate(t)
            self.update_radius(t)

    def update_weights(self, best_j: list, current_point: tuple):
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                dist = np.linalg.norm(np.asarray(best_j) - np.array([i, j]))
                radius = np.exp(-dist ** 2 / (2 * self.radius ** 2))

                self.clusters[i][j][0] += self.learning_rate * radius * (
                        current_point[0] - self.clusters[i][j][0])
                self.clusters[i][j][1] += self.learning_rate * radius * (
                        current_point[1] - self.clusters[i][j][1])

    def update_learning_rate(self, t):
        # lessen the learning rate
        self.learning_rate *= 0.9 * (1 - (t / 1000))

    def update_radius(self, t):
        self.radius *= 0.9 * (1 - (t / 1000))
