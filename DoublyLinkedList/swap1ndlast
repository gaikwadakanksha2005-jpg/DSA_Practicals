#Doubly Linear Linked List
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
        self.prev=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self, new_node):
        temp=self.head
        if temp:
            while(temp.next):
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp 
        else:#First Node
            self.head=new_node  

    def insert(self,new_node,pos):
            temp=self.head
            if pos==1:
                new_node.next=self.head
                self.head.prev=new_node
                self.head=new_node
            else:
                p=1
                while p != pos-1:
                    temp=temp.next
                    p+=1
                new_node.next=temp.next
                if temp.next:#Last position
                    temp.next.prev=new_node
                temp.next=new_node
                new_node.prev=temp

    def reverse(self):
        temp=self.head
        print("List Element:",end=" ")
        while temp :
            temp=temp.next
        while(temp):
            print(temp.data,end=" ")
            temp=temp.prev

    def del_node(self,value):
        temp=self.head
        if temp.data==value:
            self.head=self.head.next
            self.head.prev=None

        else: 
            while(temp.data!=value and temp):
                temp=temp.next
                    
                if temp==None:
                    print("\nValue is not present")
                    return
            temp.prev.next=temp.next
            if temp.next: #Not the last Node
                temp.next.prev=temp.prev
            temp=None

    def occurance(self,num):
        count=0
        temp=self.head
        while temp:
            if temp.data==num:
                count+=1
            temp=temp.next
        print("\nOccurance of", num ,"is" ,count )

    def swap(self):
        node1=self.head# node1 is first node
        temp=self.head
        while temp.next:#temp is last node
            temp=temp.next
        temp.next=node1.next
        node1.next=None
        node1.prev=temp.prev
        temp.prev.next=node1
        temp.prev=None
        self.head=temp
        


    def print(self):
        temp=self.head
        print("List Element:",end=" ")
        while temp :
            print(temp.data,end=" ")
            temp=temp.next

list=LinkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.append(Node(20))
list.insert(Node(25),3)
list.print()
#list.reverse()
list.del_node(50)
list.print()
list.occurance(10)
list.swap()
list.print()