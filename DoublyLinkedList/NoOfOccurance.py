
class Node:
    def __init__(self,value):
        self.prev=None
        self.data=value
        self.next=None

class linkedList:
    def __init__(self):
        self.head=None

    def append(self,new_node):
        temp=self.head
        if temp:
            while temp.next:
                temp=temp.next
            temp.next=new_node
            new_node.prev=temp
        else:
            self.head=new_node

    # insert at any position
    def insert(self,new_node,pos):
        temp=self.head
        if pos==1:
            new_node.next=self.head
            if self.head:
                self.head.prev=new_node
            self.head=new_node
        else:
            p=1
            while(p!=pos-1 and temp.next):
                temp=temp.next
                p+=1

            new_node.next=temp.next

            if temp.next:
                temp.next.prev=new_node

            temp.next=new_node
            new_node.prev=temp

    def delete(self,value):
        temp=self.head

        if temp is None:
            print("List is empty")
            return

        if temp.data==value:  # first node to delete
            self.head=self.head.next
            if self.head:
                self.head.prev=None
        else:
            while(temp and temp.data!=value):
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
        print("\n list of elements:")

        if temp is None:
            print("List is empty")
            return

        while temp.next:
            temp=temp.next

        while temp:  # reverse the node
            print(temp.data,end=" ")
            temp=temp.prev

        print()

    def count_occ(self,num):
        temp=self.head
        count=0

        while temp:
            if temp.data==num:
                count+=1
            temp=temp.next
        print("Occurrence of",num,"is",count)


list=linkedList()
list.append(Node(10))
list.append(Node(20))
list.append(Node(30))
list.append(Node(40))
list.print()
list.insert(Node(10),3)
list.print()
list.delete(20)
list.count_occ(10)
list.print()
