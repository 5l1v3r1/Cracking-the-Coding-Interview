# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (eg, if you have a tree with depth D, you’ll have D linked lists)
from treesAndGraphs.createBST import createBST
from collections import deque
from treesAndGraphs.createBST import Node

def createLinkedList(head):
    queue = deque([(head, 0)])

    curr = Node(0)
    root = curr

    while queue:
        (head, depth) = queue.popleft()

        if depth != curr.data:
            curr.left = Node(depth)
            curr = curr.left

        newNode = Node(head.data)
        newNode.right = curr.right
        curr.right = newNode

        if head.left:
            queue.append((head.left, depth+1))
        if head.right:
            queue.append((head.right, depth+1))

    return root


if __name__ == '__main__':
    array = [i for i in range(100)]
    head = createBST(array)

    l = createLinkedList(head)

    print(l.right)
    print(l.left.right)
    print(l.left.right.right)

