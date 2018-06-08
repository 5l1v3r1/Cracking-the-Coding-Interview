def printSquare(square):
    for row in square:
        for i in row:
            print(i, end='\t')
        print('')
    print(''.join(['-' for i in range(40)]))

def makeRowColumnZero(matrix, i, j):
    size = len(matrix[i])
    matrix[i] = [0 for i in range(size)]
    for a in range(size):
        matrix[a][j] = 0

def findPos(matrix, item):
    size = len(matrix)
    for i in range(size):
        for j in range(size):
            if matrix[i][j] == item:
                return (i, j)

if __name__ == '__main__':
    m = [[j * 10  + i for i in range(10)] for j in range(10)]
    makeRowColumnZero(m, *findPos(m, 0))
    printSquare(m)