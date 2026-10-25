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
            print("popped Element")
            self.top=self.top.next
            temp=None

    def print(self):
        if self.isempty():
            print("Empty")
        else:
            temp=self.top
            while temp:
                print(temp.data)
                temp=temp.next

s1=Stack()   
s1.push(Node(10))                                
s1.push(Node(20))  
s1.push(Node(30))  
s1.print()
s1.pop()
s1.print()