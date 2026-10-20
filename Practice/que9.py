s=input("Enter a string:")
vowels=0
consonents=0
digits=0
special=0

for ch in s:
    if ch.isalpha():
        if ch.lower() in "aeiou":
            vowels=vowels+1
        else:
            consonents=consonents+1
    elif ch.isdigit():
        digits=digits+1
    else:
        special=special+1               

print("Vowels:",vowels)
print("Consonents:",consonents) 
print("Digits:",digits) 
print("Special Characters:",special)      