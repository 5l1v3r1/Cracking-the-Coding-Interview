# You are given two sorted arrays, A and B, and A has a large enough bu er at the end to hold B Write a method to merge B into A in sorted order
import random

def merge1(a, b):
    i = 0
    j = 0

    c = []
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    for x in range(i, len(a)):
        c.append(a[x])
    for y in range(j, len(b)):
        c.append(b[j])

    return c

if __name__ == '__main__':
    a = [random.randint(1,100) for _ in range(30)]
    b = [random.randint(1,100) for _ in range(20)]

    a.sort()
    b.sort()

    print(a)
    print(b)
    print(merge1(a, b))
