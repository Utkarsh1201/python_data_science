a = int(input("Enter a number: "))
b = int(input("Enter a second number: "))
c = int(input("Enter a third number: "))
if(a>b):
    if(a>c):
        print("A is the largest number ")
    else:
        print("C is the largest number" )
else:
    if(b>c):
        print("B is the largest number")
    else:
        print("C is the largest number ")
if(a<b):
    if(a<c):
        print("A is the smallest number ")
    else:
        print("C is the smallest number" )
else:
    if(b<c):
        print("B is the smallest number")
    else:
        print("C is the smallest number ")