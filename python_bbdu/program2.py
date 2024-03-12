name=input("Enter Your Name")
rollno=int(input("Enter your Roll No."))
m1=int(input("Enter Marks obtained in Physics"))
m2=int(input("Enter Marks obtained in Chemistry"))
m3=int(input("Enter Marks obtained in Math"))
m4=int(input("Enter Marks obtained in Computer"))
m5=int(input("Enter Marks obtained in English"))
sum=m1+m2+m3+m4+m5
per=sum/5
print("**************************************ISC Result-2024*********************************************************")
print("Roll No=",rollno, "Student Name=",name)
print("Statements of Marks*")
print("Physics=",m1,"Chemistry=",m2,"Mathematics=",m3)
print("Computer=",m4,"English=",m5)
print("*********************************************************************************************************")
print("Total Marks Obtained=",sum,"/500")
print("Percentage Marks Obtained=",per,"%")
print("*****************************************************************************************************")
print("Result is ")
if(per>=90 and per<=100):
    print("Division=Distinction")
elif(per>=60 and per<90):
    print("Division=First")
elif(per>=45 and per<60):
    print("Division=Second")   
elif(per>=33 and per<45):
    print("Division=Third")
else:
    print("Sorry, You are not pass")
print("******************************************************************************************************")