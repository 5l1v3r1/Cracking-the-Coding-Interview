class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __len__(self):
        result = 0
        node = llist.head
        while node != None:
            result += 1
            node = node.next
        return result

    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def push_back(self, data):
        newNone = self.Node(data)

        if self.head == None:
            self.head = newNone
            newNone.prev = self.head

        newNone.prev = self.tail
        if self.tail != None:
            self.tail.next = newNone

        self.tail = newNone


if __name__ == '__main__':
    llist = LinkedList()
    llist.push_back(1)
    llist.push_back(2)
    llist.push_back(3)
    llist.push_back(4)
    llist.push_back(5)

    node = llist.head
    while node != None:
        print(node.data)
        node = node.next


