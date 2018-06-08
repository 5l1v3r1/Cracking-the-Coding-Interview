# Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees Can you do this in place?

def printSquare(square):
    for row in square:
        for i in row:
            print(i, end='\t')
        print('')
    print(''.join(['-' for i in range(40)]))

def rotateSquare1(square):
    size = len(square)
    result = [[j*size+i for i in range(size)] for j in range(size)]

    for i in range(size):
        for j in range(size):
            result[i][j] = square[j][size-i-1]

    return result

def rotateSquare2(square):
    size = len(square)
    for i in range(size):
        for j in range(size):
            if j >= i:
                square[i][j], square[j][size-i-1] = square[j][size-i-1], square[i][j]
    return square

if __name__ == '__main__':
    a = [[j*10+i for i in range(10)] for j in range(10)]
    printSquare(a)
    printSquare(rotateSquare1(a))
    printSquare(rotateSquare2(a))
