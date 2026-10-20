s=input("Enter a String:")
sub=input("Enter a substring:")
count=0
position=0

while True:
    position=s.find(sub,position)
    if position == -1:
        break
    count=count+1
    position=position+1
print("Number of occurance in string: ",count)

