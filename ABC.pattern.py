n=int(input("Enter a Number:"))
num=0
for i in range(n):
    for j in range(i+1):
        print(chr(65+num),end=" ")
        num=num+1
    print()  