# You have two numbers represented by a linked list, where each node contains a sin- gle digit The digits are stored in reverse order, such that the 1’s digit is at the head of the list Write a function that adds the two numbers and returns the sum as a linked list
from linkedLists.linkedList import LinkedList

def linkedListSum(a, b):
    result = LinkedList()

    head1 = a.head
    head2 = b.head
    c = 0
    while head1 != None and head2 != None:
        sumOfNodes = head1.data + head2.data
        s = sumOfNodes % 10
        result.push_back(s + c)
        c = sumOfNodes // 10

        head1 = head1.next
        head2 = head2.next

    return result


if __name__ == '__main__':
    a = LinkedList()
    a.push_back(3)
    a.push_back(1)
    a.push_back(2)

    b = LinkedList()
    b.push_back(3)
    b.push_back(0)
    b.push_back(5)

    c = linkedListSum(a, b)
    node = c.head
    while node != None:
        print(node.data)
        node = node.next
