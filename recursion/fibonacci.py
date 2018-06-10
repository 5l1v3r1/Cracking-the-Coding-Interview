# 1 1 2 3 5 8

def fibo():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def getNthFibo1(n):
    f = fibo()
    for i in range(n-1):
        next(f)
    return next(f)

def getNthFibo2(n):
    if n == 1: return 1
    if n == 2: return 1
    if n > 2: return getNthFibo2(n-1) + getNthFibo2(n-2)
    return -1

if __name__ == '__main__':
    print(getNthFibo1(5))
    print(getNthFibo2(5))