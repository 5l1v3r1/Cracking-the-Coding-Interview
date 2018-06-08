# Buggy
def mergeSorted(start1, end1, start2, end2):
    node1 = start1
    node2 = start2

    newHead = LinkedList.Node()
    while node1 != end1 and node2 != end2:
        if node1.data > node2.data:
            newHead.next = node1
            pass
        else:
            pass

def getMiddle(start, end):
    size = 0
    node = llist.head
    while node != end:
        size += 1
        node = node.next

    node = llist.head
    for i in range(size//2):
        node = node.next
    return node

def mergeSort(start, end):
    if start == end or start.next == end:
        return

    middle = getMiddle(start, end)
    mergeSort(start, middle)
    mergeSort(middle.next, end)
