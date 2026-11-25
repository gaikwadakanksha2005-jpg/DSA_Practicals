class Node:
    def __init__(self,value):
        self.left=None
        self.data=value
        self.right=None

class BST:
    def __init__(self):
        self.root=None
        self.lcnt=0
        self.cnt=0

    def insert(self,New_node):
        if self.root is None:
            self.root=New_node
        else:
            temp=self.root

            while True:
                if New_node.data<temp.data:
                    if temp.left is None:
                        temp.left=New_node
                        return
                    else:
                        temp=temp.left
                else:        
                    if temp.right is None:
                        temp.right=New_node
                        return
                    else:
                        temp=temp.right


    def inorder(self,rt):
        if rt is None:
            return
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            if rt.left is None and rt.right is None:
                self.cnt+=1
            if rt.left is not None and rt.right is not None:
                self.lcnt+=1
            self.inorder(rt.right) 

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)  
            self.preorder(rt.right) 

    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")

    def findminmax(self,rt):
        temp=rt
        while temp.left:
            temp=temp.left
        print("\n Min Node is:",temp.data)
        temp=rt
        while temp.right:
            temp=temp.right
        print("\n Max Node is:",temp.data) 

b1=BST()
b1.insert(Node(23))                                     
b1.insert(Node(300))     
b1.insert(Node(45))     
b1.insert(Node(374))     
b1.insert(Node(500))     
b1.insert(Node(3))     
b1.insert(Node(67))   
print("\n Inorder:")
b1.inorder(b1.root)
print("\n Preorder:")
b1.preorder(b1.root)
print("\n Postorder:")
b1.postorder(b1.root)
print("\n No of non leaf Node:",b1.cnt)
print("\n No of leaf Node:",b1.lcnt)



