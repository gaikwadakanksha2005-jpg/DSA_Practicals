
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def delete_middle(self):
        if self.head is None:
            print("List is empty")
            return

        # If only one node exists
        if self.head.next is None:
            self.head = None
            return

        slow = self.head
        fast = self.head
        prev = None

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # Delete the middle node
        prev.next = slow.next

    def display(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# Main program
ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original Linked List:")
ll.display()

ll.delete_middle()

print("After deleting middle node:")
ll.display()