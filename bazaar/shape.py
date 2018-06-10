import random

def show(screen):
    for row in screen:
        print(row)
    print(5*'-')

def trueCor(p, size):
    return p[0] >= 0 and p[0] < size and p[1] >= 0 and p[1] < size

def shapeCheck(map, startPoint, shapeSize):
    endPoint = (startPoint[0] + shapeSize, startPoint[1] + shapeSize)
    if not trueCor(endPoint, len(map)): return False
    for x in range(shapeSize):
        for y in range(shapeSize):
            if map[x][y] == 0:
                return False
    return True

def canCover(map, shapeSize):
    l = len(map)
    for i in range(l):
        for j in range(l):
            if shapeCheck(map, (i, j), shapeSize):
                return i, j
    return False

if __name__ == '__main__':
    map = [[random.randint(0, 25) for _ in range(50)] for __ in range(50)]
    show(map)
    print(canCover(map, 5))