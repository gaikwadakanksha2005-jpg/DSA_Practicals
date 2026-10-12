
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Create Linked List
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    # Delete First Node
    def delfirst(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        self.head = self.head.next
        temp = None

    # Delete Last Node using 2 pointers
    def dellast(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        prev = self.head
        temp = self.head.next

        while temp.next:
            prev = temp
            temp = temp.next

        prev.next = None
        temp = None

    # Print Linked List
    def print(self):
        print("List Elements:")
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main Program
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.append(60)

print("Original Linked List:")
ll.print()

ll.delfirst()
print("After deleting first node:")
ll.print()

ll.dellast()
print("After deleting last node:")
ll.print()