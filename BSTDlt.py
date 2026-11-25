#BST using Linked List
class Node:
    def __init__(self, value):
        self.left=None
        self.data=value
        self.right=None
class BST:
    def __init__(self):
        self.root=None
       
    def insert(self, new_node):
        if self.root is None: ##BST is empty
            self.root=new_node
        else:
            temp=self.root
            while True:
                if new_node.data<temp.data: #left subtree
                    if temp.left is None:
                        temp.left=new_node
                        return
                    else:
                        temp=temp.left
                else: #right subree
                    if temp.right is None:
                        temp.right=new_node
                        return
                    else:
                        temp=temp.right

    def del_node(self,rt,val):
        if rt is None:
            return rt
        if val<rt.data:
            rt.left=self.del_node(rt.left,val)
        elif val>rt.data:
            rt.right=self.del_node(rt.right,val) 
        else:
            if rt.left is None:    #Node with right child only
                return rt.right   
            if rt.right is None:  #Node with left child only
                return rt.left 
            #Node Has both left and right childern
            succ=self.get_suceessor(rt) 
            rt.data=succ.data
            rt.right=self.del_node(rt.right,succ.data)
        return rt

    def get_suceessor(self,temp):
        temp=temp.right
        while temp.left is not None :
            temp=temp.left
        return temp

    def search(self,key):
        temp=self.root
        while temp:
            if temp.data==key:
                return True
            elif key<temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False 
               
    def inorder(self, rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data, end=" ")
            self.inorder(rt.right)

    def preorder(self, rt):
        if rt is None:
            return
        else:
            print(rt.data, end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)
            
    def postorder(self, rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data, end=" ")

    def findminmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\nMin: ", temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\nMax: ", temp.data)


b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))
b1.insert(Node(54))
print("\nInorder:",end=" ")
b1.inorder(b1.root)
b1.root = b1.del_node(b1.root,54)
print("\nAfter Deletion:",end=" ")
b1.inorder(b1.root)
if b1.search(450):
    print("\n Found the Node")
else:
    print("\n Not Found Node")    

#Hospital patient token management.
# Scenario : A hospital maintains patient token numbers in BST.
# Eachh token number is unique, and the hospital want ti retrieve patient records of tasks:
# 1.insert the followig token number into BST:50,30,70,20,40,60,80,10
# 2.search for token 10 number
# display all token nuber in sorted order
# 4.find the smallest and largest token number
# 5.dlt token number 70 and display the updated BST  