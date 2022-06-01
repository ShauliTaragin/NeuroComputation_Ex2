import numpy as np
import json

from KSOM import KSOM


def createDataSet():
    points = []
    while len(points) != 1000:
        x = np.random.randint(0, 1000)
        y = np.random.randint(0, 1000)
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
    saveDataSet(points)
    # 1 A (1,100)
    model1a=KSOM(1,100)
    model1a.fit(points,10)
    # 1 B (10,10)
    model1b=KSOM(10,10)


