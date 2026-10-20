
n=int(input("Enter a number:"))
for i in range(n):
    for j in range(i):
        print(chr(64+i),end=" ")
    print()    