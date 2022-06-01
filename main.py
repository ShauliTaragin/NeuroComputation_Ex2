import numpy as np
import json
import matplotlib.pyplot as plt
from KSOM import KSOM


def createDataSet(condition):
    points = []
    if condition == 1:
        while len(points) != 1000:
            x = np.random.randint(0, 1000)
            y = np.random.randint(0, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
    elif condition == 2:
        while len(points) != 1000:
            x = np.random.randint(700, 1000)
            y = np.random.randint(700, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
    elif condition == 3:
        while len(points) != 1000:
            if len(points) < 800:
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


def FitandDraw(model, data, iterations):
    model.fit(data, iterations)


if __name__ == '__main__':
    points = createDataSet(1)
    # saveDataSet(points)
    # 1 A (1,100)
    model1a = KSOM(1, 100)
    FitandDraw(model1a, points, 10)
    # 1 B (10,10)
    # model1b=KSOM(10,10)
    # FitandDraw(model1a , points)
    # # 1 C Non uniform a
    # points = createDataSet(2)
    # model1c = KSOM(1, 15)
    # FitandDraw(model1c, points)
    # # 1 D Non uniform b
    # points = createDataSet(3)
    # FitandDraw(model1c, points)
