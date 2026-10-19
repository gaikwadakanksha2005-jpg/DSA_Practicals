class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None
class linkedList:
    def __init__(self):
        self.head=None
    def   append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node
    #insert at any position
    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1
                new_node.next=temp.next
           
            if temp.next:#for last position(this wont be executed)
                temp.next.prev=new_node
            temp.next=new_node 
            new_node.prev=temp  

    def delete(self, value):
        temp=self.head
        if temp.data==value:# first node to delete
            self.head=self.head.next
            self.head.prev=None
        else:
            while(temp.data!=value and temp):
                temp=temp.next
                if temp==None:
                    print("Value is not present in the list")
                    return
            temp.prev.next=temp.next
            if temp.next:
                temp.next.prev=temp.prev
            temp=None            
    
    def print(self):
            temp=self.head
            print("list of elements:")            
            while temp.next:
                #print(temp.data,end =" ")(for reverse)
                temp=temp.next
            while (temp):#reverse the node
                print(temp.data,end =" ")
                temp=temp.prev


list=linkedList()
list.append(Node(12))
list.append(Node(52))
list.append(Node(102))
list.append(Node(56))
list.print()
list.insert(Node(40),3)
list.print()
list.delete(102)
list.print()