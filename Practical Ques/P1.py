
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

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

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

    def delete(self):
        while self.head != None and self.head.data < 0:
            self.head = self.head.next

        temp = self.head
        while temp != None and temp.next != None:
            if temp.next.data < 0:
                temp.next = temp.next.next
            else:
                temp = temp.next

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("None")


ll = LinkedList()
# 1. Create Linked List
n = int(input("Enter number of nodes: "))

for i in range(n):
    val = int(input("Enter node value: "))
    ll.append(Node(val))

print("Append List:")
ll.print()

# 2. Traverse
print("Traversing List:")
ll.traverse()

# 3. Insert at specific position
val = int(input("Enter value to insert: "))
pos = int(input("Enter position: "))
ll.insert(Node(val), pos)
print("Insert at specific position:")
ll.print()

# 4. Delete negative nodes
ll.delete()
print("Delete negative nodes:")
ll.print()
