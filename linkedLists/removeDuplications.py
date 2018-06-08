from linkedLists.linkedList import LinkedList


# use hash set
def removeDuplication(llist):
    hit = dict()

    node = llist.head

    while node != None:
        if node.data not in hit:
            hit[node.data] = True
        else:
            if node.prev != None:
                node.prev.next = node.next
            if node.next != None:
                node.next.prev = node.prev
        node = node.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(5)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(3)
    llist.push_back(4)
    llist.push_back(5)
    llist.push_back(5)

    removeDuplication(llist)

    node = llist.head
    while node != None:
        print(node.data)
        node = node.next



