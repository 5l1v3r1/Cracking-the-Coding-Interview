# Imagine a robot sitting on the upper left hand corner of an NxN grid The robot can only move in two directions: right and down How many possible paths are there for the robot?

def numOfPathes(n, m=None):
    if m == None: m = n
    if n == 1 or m == 1: return 1
    return numOfPathes(n-1, m) + numOfPathes(n, m-1)

if __name__ == '__main__':
    print(numOfPathes(3))