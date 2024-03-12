import math
#program to calculate and print roots of quadratic equation ax2+bx+c=0
a=int(input("enter value of a"))
b=int(input("enter value of b"))
c=int(input("enter value of c"))
d=math.pow(b,2)-(4*a*c)
if(d<0):
    print("Roots are imaginary")
elif(d==0):
    r1=r2=(-b/(2*a))
    print("Roots are real and equal")
    print("Postive Root=",r1,"and Negative Root=",r2)
else:
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Roots are real and unequal")
    print("Postive Root=",r1,"and Negative Root=",r2)