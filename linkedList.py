# def printLinkedList(head):

#     return


# if __name__ == '__main__':
#     llist_count = int(input())

#     llist = SinglyLinkedList()

#     for _ in range(llist_count):
#         llist_item = int(input())
#         llist.insert_node(llist_item)

#     printLinkedList(llist.head)

#     class SinglyLinkedListNode:
#         def __init__(self, data):
#             self.data = data
#             self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = SinglyLinkedListNode(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


def printLinkedList(head):
    current = head
    while current:
        print(current.data)
        current = current.next


if __name__ == '__main__':
    llist_count = int(
        input("Enter the number of elements in the linked list: "))

    llist = SinglyLinkedList()

    print("Enter the elements:")
    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    print("Linked List elements:")
    printLinkedList(llist.head)
