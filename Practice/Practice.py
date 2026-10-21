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
        print("None")                    
        print("count:",self.count)
l1=LinkedList()
l1.append(Node(10))        
l1.append(Node(20))  
l1.append(Node(30))  
l1.append(Node(40))  
l1.print()
l1.insert(Node(100),1)
l1.print()