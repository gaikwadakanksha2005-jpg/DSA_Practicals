
class Node:
    def __init__(self, value):
        self.prev = None
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp
        else:
            self.head = new_node

    def print(self):
        temp = self.head
        print("List Of Elements:")
        while temp:
            print(temp.data,end=" ")
            temp = temp.next 

list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(15))
list1.append(Node(20))
list1.append(Node(25))
list1.print()
