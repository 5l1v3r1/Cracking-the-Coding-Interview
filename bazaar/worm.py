import sys
import time

import operator

delta = [
        (-1, 0),
        (0, -1),
        (1, 0),
        (0, 1)
    ]

def sum(a, b):
    return (a[0] + b[0], a[1] + b[1])

def show(screen):
    for row in screen:
        print(row)
    print(5*'-')

def isTrueCor(x, y, size):
    return x >= 0 and x < size and y >= 0 and x < size

def isLeftFree(hitMap, x, y, d, l):
    global delta

    leftSide = (d + 1) % 4
    seePoint = sum((x, y), delta[leftSide])

    if not isTrueCor(seePoint[0], seePoint[1], l):
        return False

    return not hitMap[seePoint[0]][seePoint[1]]

def go(map, x, y, d=0):
    global delta

    hitMap = [[False for _ in row] for row in map]
    l = len(map)

    while isTrueCor(x, y, l):
        hitMap[x][y] = True
        print(map[x][y])
        show(hitMap)

        if isLeftFree(hitMap, x, y, d, l):
            d = (d + 1) % 4

        x, y = sum((x, y), delta[d])

if __name__ == '__main__':
    sys.setrecursionlimit(1000000)
    map = [[i+(j*10) for i in range(10)] for j in range(10)]
    mid = len(map) // 2
    go(map, mid, mid)