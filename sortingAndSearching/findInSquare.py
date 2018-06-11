def findInRowColumn(arr, item, x, y):
    for i in range(0, len(arr[0])):
        if arr[x][i] == item:
            return (x, i)

    for j in range(0, len(arr)):
        if arr[j][y] == item:
            return (x, j)

def findInMap(arr, item, minX=None, maxX=None, minY=None, maxY=None):
    if minX is None:
        minX, maxX = 0, len(arr[0])
        minY, maxY = 0, len(arr)

    if maxX - minX < 2:
        return findInRowColumn(arr, item, maxX, maxY)

    midX = (minX + maxX) // 2
    midY = (minY + maxY) // 2

    f = findInRowColumn(arr, item, midX, minY)
    if f:
        return f

    if arr[midX][midY] > item:
        return findInMap(arr, item, minX, midX-1, minY, midY-1)
    else:
        return findInMap(arr, item, midX+1, maxX, midY+1, maxY)



if __name__ == '__main__':
    arr = [[1, 2, 3, 4, 5],
           [3, 4, 5, 6, 7],
           [4, 5, 6, 7, 8],
           [7, 8, 9,12,13],
           [10,15,20,25,30]]


    print(findInMap(arr, 10))