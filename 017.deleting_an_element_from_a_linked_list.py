"""
Deleting a node from a linked list

Create a function to remove a node from the given linked list.
The function must traverse the linked list to find the node to be deleted.

You do not need to return the linked list that went through the deletion
because you can directly delete the node from the given linked list.

NOTE: there is no duplicate number in the linked list.
"""


class Node:
    """
    The 'Node' class for a singly linked list.

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


def toArray(llNode):
    array = []

    head_node = llNode.head

    while head_node != llNode.tail:
        array.append(head_node.val)
        head_node = head_node.next

    array.append(head_node.val)

    return array


# Convert the given array to a linked list.

def toLinkedList(lst):
    """
    The 'toLinkedList' class converts the given array into a linked list then returns it.

    NOTE: lst[0] is wrapped into the 'Node' class object.
    """

    llNode = LinkedList(Node(lst[0]))

    for i in lst[1:]:
        llNode.addToEnd(Node(i))  # i: the data that represents the index.

    return llNode


def deleteNode(ll, valToDelete):
    """
    When the head node is the same with the element 'valToDelete',
    you can delete the head node by designating the second node as the head node.
    """

    if ll.head.val == valToDelete:  # ll.head == valToDelete (X)  ll.head.val == valToDelete (O)
        ll.head = ll.head.next

    current_node = ll.head
    next_node = current_node.next

    while next_node:
        """
        If 'next_node' exists, check if its value is the same with 'valToDelete'.
        If the value of next_node == valToDelete,
        set the next node of current node to 'next_node.next' to remove current 'current_node'.
        """
        if next_node.val == valToDelete:
            current_node.next = next_node.next

            """
            When the pointer reaches the tail node of the linked list, the loop will be terminated.
            To safely break the loop, if 'current_node' is the tail node or not must be checked.
            """
            if next_node == ll.tail:
                ll.tail = current_node

            break

        current_node = current_node.next
        next_node = current_node.next


def main():
    nums = [2, 8, 19, 37, 4, 5]
    ll = toLinkedList(nums)
    print(ll)
    deleteNode(ll, 19)
    print(ll)  # 19 is deleted. Thus, 2->8->37->4->5
    deleteNode(ll, 3)
    print(ll)  # There is no 3. Thus, 2->8->37->4->5


if __name__ == "__main__":
    main()