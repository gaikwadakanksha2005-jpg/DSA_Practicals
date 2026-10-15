
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

    def insert(self,new_node,pos):
        temp=self.head
        if pos==1: 
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1):
                temp=temp.next
                p+=1
            new_node.next=temp.next
          
            if temp.next:   #last position
                temp.next.prev=new_node   
            temp.next=new_node 
            new_node.prev=temp    
            
    def print(self):
        temp = self.head
       
        print("List Of Elements:")
        while temp.next:
            temp=temp.next
        while temp:
            print(temp.data,end=" ")
            temp = temp.prev 

list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(15))
list1.append(Node(20))
list1.append(Node(25))
list1.insert(Node(40),3)
list1.print()

