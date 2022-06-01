import numpy as np
import json
import matplotlib.pyplot as plt
from KSOM import KSOM


def createDataSet(condition):
    """
    Creating Data set according to differnet cases
    :param condition: cases:
    1 : uniform distribution (for regular case and 10x10 on a 2D plane)
    2 : non uniform distribution on a liner plane example 1
    3 : non uniform distribution on a liner plane example 2
    4 : Donut
    5 : Monkey hand
    6 : Cut off monkey hand
    """

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
    elif condition == 5:  # hand with all fingers
        for j in range(200):
            x = np.random.randint(100, 200)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for j in range(200):
            x = np.random.randint(300, 400)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for j in range(200):
            x = np.random.randint(500, 600)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for j in range(200):
            x = np.random.randint(700, 800)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for i in range(1000):
            x = np.random.randint(100, 800)
            y = np.random.randint(0, 400)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
    elif condition == 4: # donut
        while len(points) != 1000:
            x = np.random.randint(-10000, 10000)
            y = np.random.randint(-10000, 10000)
            if (x / 1000, y / 1000) not in points and 2 <= (x / 1000) ** 2 + (y / 1000) ** 2 <= 4:
                points.append((x / 1000, y / 1000))
    elif condition == 6: # cut off hand
        for j in range(200):
            x = np.random.randint(100, 200)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for j in range(200):
            x = np.random.randint(500, 600)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for j in range(200):
            x = np.random.randint(700, 800)
            y = np.random.randint(400, 1000)
            if (x / 1000, y / 1000) not in points:
                points.append((x / 1000, y / 1000))
        for i in range(1000):
            x = np.random.randint(100, 800)
            y = np.random.randint(0, 400)
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
    points = createDataSet(1)
    # saveDataSet(points)
    # 1 A (1,100)
    model1a = KSOM(1, 100)
    model1a.fit(points, 250)
    # 1 B (10,10)
    model1b = KSOM(10, 10)
    model1b.fit(points, 250)
    # 1 C Non uniform a
    points = createDataSet(2)
    model1c = KSOM(1, 100)
    model1c.fit(points, 1000)
    # 1 D Non uniform b
    points = createDataSet(3)
    model1c.fit(points, 500)
    # 1 E Donut
    points = createDataSet(4)
    model1e = KSOM(1, 30)
    model1e.fit(points, 250)
    # 2 A Monkey hand
    points = createDataSet(5)
    model2a = KSOM(15, 15)
    model2a.fit(points, 250)
    # 1 E Cut off Monkey hand
    points = createDataSet(6)
    model2b = KSOM(model2a, model2a)
    model2b.fit(points, 250)
