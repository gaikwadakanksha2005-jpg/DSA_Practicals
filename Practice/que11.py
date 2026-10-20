s=input("Enter a string:")
words=s.split()
for word in words:
    print(word[::-1],end="")