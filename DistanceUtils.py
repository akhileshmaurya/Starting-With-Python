import math


def manhatanDistance(x1, y1, x2, y2):
    distance = math.abs(x1 - x2) + math.abs(y1 - y2)
    return distance


def euclidianDistance(x1, y1, x2, y2):
    distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return distance
