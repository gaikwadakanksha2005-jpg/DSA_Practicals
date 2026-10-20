n=int(input("Enter number:"))
a=[0]*n
print("Enter a number:")
count=0
for i in range(n):
    a[i]=int(input())
even=0
odd=0

for i in range(n):
    if i % 2 == 0:
        even=even+1
    else:
        odd=odd+1
print("Even:",even)
print("odd:",odd)        
