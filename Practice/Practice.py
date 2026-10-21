class Node:
    def __init__(self,val):
        self.data=val
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.count=0

    def append(self,new_node):
        if self.head==None:
            self.head=new_node
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
        self.count=self.count+1    

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head=new_node
            return
        p=1
        while p!=pos-1 and temp.next!=None:
            temp=temp.next
            p+=1
        new_node.next=temp.next
        temp.next=new_node

    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print("none")
        print("total count:",self.count)   

list=LinkedList()   
n1=Node(20)    
list.append(n1)                         
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.print()
print("After Insertion:")
list.insert(Node(50),4)
list.insert(Node(100),2)
list.print()