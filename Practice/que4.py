n=int(input("Enter a number:"))
a=[0]*n
print("enter number:")
for i in range(n):
    a[i]=int(input())
s=int(input("Enter a search number:"))    
found=0
for i in range(n):
    if a[i] == s:
        print("element found position:",i+1)
        found=1
        break
    if found==0:
        print("element not found position:",i+1)
    
