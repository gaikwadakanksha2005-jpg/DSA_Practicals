
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

    # Concatenate two linked lists
    def concatenate(self, list2):
        if self.head is None:
            self.head = list2.head
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = list2.head

    # Print Linked List
    def print(self):
        temp = self.head

        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

        print("None")


# First Linked List
ll1 = LinkedList()
ll1.append(10)
ll1.append(20)
ll1.append(30)

# Second Linked List
ll2 = LinkedList()
ll2.append(40)
ll2.append(50)
ll2.append(60)

print("First Linked List:")
ll1.print()
print("Second Linked List:")
ll2.print()
# Concatenate
ll1.concatenate(ll2)
print("After Concatenation:")
ll1.print()