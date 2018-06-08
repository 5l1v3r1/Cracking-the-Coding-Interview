from treesAndGraphs.tree import Node

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

