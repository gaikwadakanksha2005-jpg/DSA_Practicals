n=int(input("Enter a number:"))
a=[0]
print("Enter number:")
for i in range(n):
  a[i]=int(input())
  largest=a[0]
  smallest=a[0]

for i in range(1,n):
  if a[i]>largest:
    largest=a[i]
    if a[i]<smallest:
      smallest=a[i]
    second_largest=a[0]   
    second_smallest=a[0]

    for i in range(n):
      if a[i]!=largest and a[i]>second_largest:
        second_largest=a[i]


    for i in range(n):
      if a[i]!=smallest and a[i]>second_smallest:
        second_smallest=a[i]
    print("largest:",largest)
    print("second largest:",second_largest)   
    print("smallest:",smallest) 
    print("Second largest:",second_largest)