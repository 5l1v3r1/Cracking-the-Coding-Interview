# Buggy

from collections import deque
import copy
import time

def showTowers(a, b, c, size=5):
    a, b, c = copy.deepcopy((a, b, c))
    maxLen = max(len(a), len(b), len(c), size)
    a += ['a' for i in range(maxLen - len(a))]
    b += ['b' for i in range(maxLen - len(b))]
    c += ['c' for i in range(maxLen - len(c))]

    for i in range(maxLen-1, -1, -1):
        print('{}\t{}\t{}'.format(a[i], b[i], c[i]))

    print('----------------')

def moveOne(a, b):
    print('move one: ', a, b)
    t = a.pop()
    b.append(t)

def move(a, b, c, count):
    showTowers(a, b, c, 6)
    time.sleep(1)
    if count == 1:
        moveOne(a, b)
    else:
        move(a, b, c, count-1)
        moveOne(a, c)
        move(b, c, a, count-1)

if __name__ == '__main__':
    a = deque()
    b = deque()
    c = deque()

    a.append(5)
    a.append(4)
    a.append(3)
    a.append(2)
    a.append(1)

    move(a, c, b, 2)

    showTowers(a, b, c, 6)

