n=int(input("Enter a num:"))
a=[]
print("Enter element:")
for i in range(n):
    a.append(int(input()))
    sum=0
for i in range(n):
    sum=sum+a[i]
print(sum)        