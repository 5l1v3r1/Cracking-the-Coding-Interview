from linkedLists.linkedList import LinkedList

def findMitting(llist):
    head1 = llist.head
    head2 = llist.head.next

    while head1 != head2:
        head1 = head1.next
        head2 = head2.next.next

    return head1

if __name__ == '__main__':
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    llist.push_back(5)


    node = llist.head
    node = node.next
    x = node.next

    llist.tail.next = x

    print(findMitting(llist).data)
    #
    # node = llist.head
    # while node != None:
    #     print(node.data)
    #     node = node.next

