# Implement a function to check if a tree is balanced For the purposes of this question, a balanced tree is de ned to be a tree such that no two leaf nodes di er in distance from the root by more than one

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def addRight(self, node):
        self.right = node

    def addLeft(self, node):
        self.left = node


def maxDepth(root):
    if root == None:
        return 0
    else:
        return 1 + max(maxDepth(root.left), maxDepth(root.right))

def minDepth(root):
    if root == None:
        return 0
    else:
        return 1 + min(minDepth(root.left), minDepth(root.right))

def isTreeBalanced(root):
    if root == None:
        return True
    else:
        return maxDepth(root) - minDepth(root) <= 1

if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    t = Node('t')

    a.addLeft(b)
    a.addRight(c)
    b.addLeft(d)
    c.addRight(e)

    print(isTreeBalanced(a))

    e.addRight(t)
    print(isTreeBalanced(a))

