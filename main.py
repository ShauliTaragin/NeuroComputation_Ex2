import numpy as np
import json
import matplotlib.pyplot as plt
from KSOM import KSOM


def createDataSet(condition):
    points = []
    if condition == 1 :
        while len(points) != 1000:
            x = np.random.randint(0, 1000)
            y = np.random.randint(0, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
    elif condition==2:
        while len(points) != 1000:
            x = np.random.randint(700, 1000)
            y = np.random.randint(700, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
    elif condition == 3:
        while len(points) != 1000:
            if len(points)<800:
                x = np.random.randint(0, 200)
                y = np.random.randint(0, 200)
            else:
                x = np.random.randint(800, 1000)
                y = np.random.randint(800, 1000)
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
def FitandDraw(model , points):
    x_points = [x[0] for x in points]
    y_points = [y[1] for y in points]
    x_model_a = []
    y_model_a = []
    model.fit(points, 100)
    for i in range(model.shape[0]):
        for j in range(model.shape[1]):
            x_model_a.append(model.clusters[i][j][0])
            y_model_a.append(model.clusters[i][j][1])
    plt.scatter(x_points, y_points, color="blue", s=70, alpha=0.5)
    plt.scatter(x_model_a, y_model_a, color="red")
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.show()

if __name__ == '__main__':
    points = createDataSet(1)
    #saveDataSet(points)
    # 1 A (1,100)
    model1a=KSOM(1,100)
    FitandDraw(model1a , points)
    # 1 B (10,10)
    model1b=KSOM(10,10)
    FitandDraw(model1a , points)
    # 1 C Non uniform a
    points = createDataSet(2)
    model1c = KSOM(1, 15)
    FitandDraw(model1c, points)
    # 1 C Non uniform b
    points = createDataSet(3)
    FitandDraw(model1c, points)



