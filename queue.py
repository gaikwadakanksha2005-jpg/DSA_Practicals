class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def  enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        print("Delete Node:",temp.data)
        self.front=self.front.next
        if self.front==None:
            print("Queue is empty")
            self.rear=None

    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print()

que=Queue()
que.enqueue(Node(10))                                   
que.enqueue(Node(20))   
que.enqueue(Node(30))   
que.enqueue(Node(40))   
que.enqueue(Node(50))   
que.print()
que.dequeue()
que.dequeue()
que.print()