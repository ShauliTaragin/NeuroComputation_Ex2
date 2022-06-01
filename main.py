import numpy as np
import json
import matplotlib.pyplot as plt
from KSOM import KSOM


def createDataSet():
    points = []
    while len(points) != 1000:
        x = np.random.randint(700, 1000)
        y = np.random.randint(700, 1000)
        if (x / 1000, y / 1000) not in points:
            points.append((x / 1000, y / 1000))
    return points


def saveDataSet(DataSetPoints):
    data = {}
    for i in range(len(DataSetPoints)):
        data[str(i)] = {"x": DataSetPoints[i][0], "y": DataSetPoints[i][1]}
    with open('dataset1.json', 'w') as f:
        json.dump(data, f)
        print("saved")


if __name__ == '__main__':
    points = createDataSet()
    #saveDataSet(points)
    # 1 A (1,100)
    model1a=KSOM(1,15, num_of_clusters=15)
    x_points = [x[0] for x in points]
    y_points = [y[1] for y in points]
    x_model_a = []
    y_model_a = []
    model1a.fit(points,100)
    for i in range(model1a.shape[0]):
        for j in range(model1a.shape[1]):
            x_model_a.append(model1a.clusters[i][j][0])
            y_model_a.append(model1a.clusters[i][j][1])
    plt.scatter(x_points,y_points,color = "blue",s=70, alpha=0.5)
    plt.scatter(x_model_a,y_model_a,color ="red")
    plt.show()
    # 1 B (10,10)
    # model1b=KSOM(10,10)
    # model1b.fit(points,10)
    # x_model_b = []
    # y_model_b = []
    # for i in range(model1b.shape[0]):
    #     for j in range(model1b.shape[1]):
    #         x_model_b.append(model1b.clusters[i][j][0])
    #         y_model_b.append(model1b.clusters[i][j][1])
    # plt.scatter(x_points, y_points, color="blue", s=70, alpha=0.5)
    # plt.scatter(x_model_b, y_model_b, color="red")
    # plt.show()



