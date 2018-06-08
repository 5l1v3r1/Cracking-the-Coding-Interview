# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node

    def __str__(self):
        return str(self.data)


def createBST(array):
    if len(array) == 1:
        return Node(array)
    elif len(array) == 0:
        return None

    mid = len(array) // 2
    right = array[mid+1:]
    left = array[:mid]

    m = array[mid]
    l = createBST(left)
    r = createBST(right)

    head = Node(m)
    head.addRight(r)
    head.addLeft(l)

    return head


if __name__ == '__main__':
    array = [i for i in range(100)]
    head = createBST(array)

    print(head)
    print(head.left)
    print(head.right)