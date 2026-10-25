class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        print("delete Node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Empty")
            self.rear=None
    def print(self):
        temp=self.front
        while temp:
            print(temp.data)
            temp=temp.next
        print()
qu=Queue()
qu.enqueue(Node(10))  
qu.enqueue(Node(20))
qu.print()
qu.dequeue()
qu.print()                
