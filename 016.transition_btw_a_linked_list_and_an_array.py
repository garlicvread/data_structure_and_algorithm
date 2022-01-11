"""
Transition between a linked list and an array

A class "LinkedList" that defines a linked list and another class "Node" that defines its nodes.

Implement a class "toArray" that returns an array when a linked list object is given
and another class "toLinkedList" that returns vice versa.
"""


class Node:
    """
    The 'Node' class for a linked list.
    This class is for a singly linked list.

    NOTE: You do not need to modify this class.
    """
    def __init__(self, val):
        self.val = val
        self.next = None

    def __str__(self):
        return str(self.val)


class LinkedList:
    """
    A linked list class 'LinkedList'.
    The class 'LinkedList' has its head, tail,
    and a function 'addToEnd' that can add a new node at the end of the list.

    NOTE: the code is already complete. You do not need to modify it.
    """
    def __init__(self, head):
        self.head = head
        self.tail = head

    def addToEnd(self, node):
        self.tail.next = node
        self.tail = node

    def __str__(self):
        node = self.head
        toPrint = []

        while node:
            toPrint.append(str(node.val))
            node = node.next
        return "->".join(toPrint)


# Convert the given linked list 'll' to an array.
# Assume that the object of 'LinkedList' will be given as the input.

def toArray(llNode):
    # Create an empty list to store the node information from the linked list.
    array = []

    # Create an element to store the head node of the linked list.
    head_node = llNode.head

    # From the head node, traverse the linked list and store the node information in the list created above.
    # While the head_node is not the tail node, append the data to the array and move to the next node.
    while head_node != llNode.tail:
        array.append(head_node.val)  # head_node.val: the data of the current node.
        head_node = head_node.next

    # When head_node is the same with the tail node, the while loop that is used above will be terminate.
    # Thus, you need to append the head_node manually when it is the same with the tail node.
    array.append(head_node.val)

    return array


# Convert the given array to a linked list.

def toLinkedList(lst):
    """
    When a list 'lst' is given, the first element of the list is the head node of the linked list.
    Using the class 'LinkedList', you can create a linked list object.
    llNode: a linked list that has the first element of given list 'lst' as its head node.

    NOTE: lst[0] must be inputted as a 'Node' class object.
    """
    llNode = LinkedList(Node(lst[0]))

    for i in lst[1:]:
        llNode.addToEnd(Node(i))  # i: the data that represents the index.

    return llNode


# Examples of using 'LinkedList' class and 'Node' class.
def example():
    ll = LinkedList(Node(3))
    ll.addToEnd(Node(4))
    ll.addToEnd(Node(8))
    print(ll)
    print(ll.head)
    print(ll.tail)


def main():
    example()
    nums = [2, 8, 19, 37, 4, 5]
    ll = toLinkedList(nums)
    print(ll)
    lst = toArray(ll)
    print(lst)


if __name__ == "__main__":
    main()
