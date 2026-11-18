class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class Stack:
    def __init__(self):
        self.top=None
    def isempty(self):
        return self.top is None            

    def push(self,new_node):
        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.isempty():
            print("Stack empty")
        else:
            temp=self.top
            popped_data=temp.data
            self.top=self.top.next
            temp=None
            return popped_data

    def print(self):
        if self.isempty():
            print("Empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

class Queue:
    def __init__(self):
        self.front=self.rear=None

    def isempty(self):
        return self.front is None
    def enqueue(self,new_node):
        if self.rear:
            self.rear.next=new_node
            self.rear=new_node
        else:
            self.front=self.rear=new_node

    def dequeue(self):
        temp=self.front
        dequed_data=temp.data
        self.front=self.front.next
        if self.front==None:
            print("Queue is Empty")
            self.rear=None
        temp=None
        return dequed_data  
    
    def print(self):
        temp=self.front
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)

def reverse_stack(s1):
    q1=Queue()
    while not s1.isempty():  #pop from stack and enqueue to queue
        q1.enqueue(Node(s1.pop()))
    #q1.print()
    while not q1.isempty():
        s1.push(Node(q1.dequeue()))
    s1.print()

s1=Stack()   
s1.push(Node(10))                                
s1.push(Node(20))  
s1.push(Node(30))  
print("original Satck:")
s1.print()
print("reverse Stack using queue:")
reverse_stack(s1)
