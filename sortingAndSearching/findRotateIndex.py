import random
from collections import deque

def findRotateIndex(arr, start=None, end=None):
    if start is None:
        start = 0
        end = len(arr) - 1

    if end - start < 2:
        return start + 1

    mid = (start + end) // 2
    if arr[mid] > arr[end]:
        return findRotateIndex(arr, mid, end)
    else:
        return findRotateIndex(arr, start, mid)

if __name__ == '__main__':
    arr = [random.randint(0, 100) for _ in range(20)]
    arr.sort()

    arr = deque(arr)
    arr.rotate(10)

    print(arr)
    print(findRotateIndex(arr))