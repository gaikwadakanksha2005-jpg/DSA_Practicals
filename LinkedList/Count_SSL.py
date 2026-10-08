class Node:
    def __init__(self, val):
        self.data = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, new_node):
        if self.head == None:
            self.head = new_node
        else:
            temp = self.head

            while temp.next != None:
                temp = temp.next

            temp.next = new_node

        self.count = self.count + 1

    def print(self):
        temp = self.head

        while temp:
            print(temp.data)
            temp = temp.next

        print("Total Node:", self.count)


list = LinkedList()

n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

list.append(n1)
list.append(n2)
list.append(n3)
list.append(n4)
list.append(Node(55))

list.print(a