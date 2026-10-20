n=int(input("Enter no of elements:"))
a=[0]*n
print("Enter number:")
for i in range(n):
    a[i]=int(input("Enter number:"))
unique=[]
for i in range(n):
    if a[i] not in unique:
        unique.append(a[i])
print("Array after duplicates:")
print(unique)

