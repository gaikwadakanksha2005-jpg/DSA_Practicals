
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next != None:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        temp = self.head

        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        p = 1
        while p != pos - 1 and temp.next != None:
            temp = temp.next
            p += 1

        new_node.next = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


list = LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
print("Original list:")
list.print()

list.insert(Node(100), 1)
print("After inserting at position 1:")
list.print()

list.insert(Node(66), 3)
print("After inserting at position 3:")
list.print()
