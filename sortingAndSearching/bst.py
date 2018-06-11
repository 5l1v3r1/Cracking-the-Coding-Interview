def binarySearch(arr, start, end, item):
    mid = (start + end) // 2
    if arr[mid] == item:
        return mid
    elif arr[mid] > item:
        return binarySearch(arr, start, mid-1, item)
    else:
        return binarySearch(arr, mid+1, end, item)


if __name__ == '__main__':
    arr = [2, 3, 4, 10, 40]
    x = 10

    result = binarySearch(arr, 0, len(arr) - 1, x)

    if result != -1:
        print("Element is present at index %d" % result)
    else:
        print("Element is not present in array")
