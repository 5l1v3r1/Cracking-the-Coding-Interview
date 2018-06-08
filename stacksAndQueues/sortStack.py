# Write a program to sort a stack in ascending order You should not make any assump- tions about how the stack is implemented The following are the only functions that should be used to write this program: push | pop | peek | isEmpty
from collections import deque

def qSort(stack):
    if len(stack) > 0:
        a = stack.pop()
        qSort(stack)
        tmp = deque()

        while len(stack) > 0 and stack[len(stack)-1] > a:
            tmp.append(stack.pop())

        stack.append(a)

        while len(tmp) > 0:
            stack.append(tmp.pop())

if __name__ == '__main__':
    q = deque()

    q.append(1)
    q.append(5)
    q.append(2)
    q.append(1)
    q.append(3)
    q.append(4)

    print(q)
    qSort(q)
    print(q)
