n=int(input("Enatr no of elements:"))
a=[0]*n
print("Enter a number:")
for i in range(n):
   a[i]=int(input())
print("original Array:",a)   
print("Reverse array:",end="")
for i in range(n-1,-1,-1):
   print(a[i],end="")


