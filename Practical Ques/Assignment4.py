
class Node: 
    def __init__(self,val): 
        self.left=None 
        self.product_id=val 
        self.right=None 
#1. Create a BST using product IDs.  
class BST: 
    def __init__(self): 
        self.root=None 
 
#Insert Product 
    def insert(self,new_product): 
        if self.root is None: 
            self.root=new_product 
            return 
        else: 
            temp=self.root 
 
            while True: 
                if new_product.product_id<temp.product_id: 
                    if temp.left is None: 
                        temp.left=new_product 
                        return 
                    else: 
                        temp=temp.left 
                else: 
                    if temp.right is None: 
                        temp.right=new_product 
                        return  
                    else: 
                        temp=temp.right 
 
#2. Display product IDs in ascending order. 
    def inorder(self,rt): 
        if rt is None: 
            return 
        else: 
            self.inorder(rt.left) 
            print(rt.product_id,end=" ") 
            self.inorder(rt.right) 
 
#3. Search for product ID 175 exists.  
    def search(self,key): 
        temp=self.root 
        while temp: 
           if temp.product_id==key: 
               return True 
           else: 
               if key<temp.product_id: 
                   temp=temp.left 
               else: 
                  temp=temp.right  
        return False           
 
#5. Display the BST using inorder, preorder, and postorder traversals. 
    def preorder(self,rt): 
        if rt is None: 
           return 
        else: 
           print(rt.product_id,end=" ") 
           self.preorder(rt.left) 
           self.preorder(rt.right) 
 

 
    
    def postorder(self,rt): 
        if rt is None: 
           return 
        else: 
           self.postorder(rt.left) 
           self.postorder(rt.right) 
           print(rt.product_id,end=" ")   
 
#6. Find the minimum and maximum product IDs.  
    def findminmax(self,rt): 
       temp=rt 
       while temp.left: 
           temp=temp.left 
       print("\n Minimum Product Id:",temp.product_id) 
       temp=rt 
       while temp.right: 
           temp=temp.right 
       print("\n Maximum Product ID:",temp.product_id)    
 
#4. Delete product ID 100.  
    def delete(self,rt,val): 
        if rt is None: 
            return rt 
        if val<rt.product_id: 
            rt.left=self.delete(rt.left,val) 
        elif val>rt.product_id: 
            rt.right=self.del_node(rt.right,val) 
        else: 
            if rt.left is None: 
                return rt.right 
            if rt.right is None: 
                return rt.left 
            succ=self.get_successor(rt) 
            rt.product_id=succ.product_id 
            rt.right=self.delete(rt.right,succ.product_id) 
        return rt 
    def get_successor(self,temp): 
        temp=temp.right 
        while temp.left is None: 
            temp=temp.left 
        return temp                  
 

#Insert the following product IDs: 150, 100, 200, 75, 125, 175, 250, 60, 90, 110. 
b1=BST() 
b1.insert(Node(150))    
b1.insert(Node(100))    
b1.insert(Node(200))    
b1.insert(Node(75))    
b1.insert(Node(125))    
b1.insert(Node(175))    
b1.insert(Node(250))    
b1.insert(Node(60))    
b1.insert(Node(90))  
b1.insert(Node(110)) 
print("\n Display Prouct IDs in ascending order:",end=" ") 
b1.inorder(b1.root) 

print("\nSearch Product ID 175:",end=" ") 
if b1.search(175): 
   print("175 is Found") 
else: 
  print(" 175 is Not Exist")  

#Inorder 
print("\n Inoder:",end=" ") 
b1.inorder(b1.root)

#Preorder 
print("\n Preorder:",end=" ") 
b1.preorder(b1.root) 

#Postorder 
print("\n Postorder:",end=" ") 
b1.postorder(b1.root) 

#Find Minimum and Maximum 
b1.findminmax(b1.root) 

#Delete 100 
b1.delete(b1.root,100) 
print("\n Delete Product ID 100:") 

#After Deletion 
print("\n After Deletion:",end=" ") 
b1.inorder(b1.root)