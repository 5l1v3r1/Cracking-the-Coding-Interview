# Implement a MyQueue class which implements a queue using two stacks
from collections import deque

class MyQueue:
    def __init__(self):
        self.main = deque()
        self.tmp = deque()

    def apend(self, value):
        self.main.append(value)

    def pop(self):
        while len(self.main) > 1:
            self.tmp.append(self.main.pop())
        result = self.main.pop()
        while len(self.tmp) > 0:
            self.main.append(self.tmp.pop())
        return result


if __name__ == '__main__':
    q = MyQueue()
    q.apend(1)
    q.apend(2)
    q.apend(3)

    print(q.pop())
    print(q.pop())
    print(q.pop())

