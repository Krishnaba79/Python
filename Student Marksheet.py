rno = int(input("Enter student Roll no. : "))
sname= input("Enter student name: ")
s1= int(input("Enter Marks of sub-1: "))
s2= int(input("Enter Marks of sub-2: "))
s3= int(input("Enter Marks of sub-3: "))
s4= int(input("Enter Marks of sub-4: "))
s5= int(input("Enter Marks of sub-5: "))

total= s1+s2+s3+s4+s5
percentage= total/5
print("student name : ",sname)
print("student roll no. : ",rno)
print("Total Marks : ",total,"/500")
print("Percentage : ",percentage)
if percentage>80:
    grade= "A"
elif percentage>60:
    grade= "B"
elif percentage>50:
    grade= "C"
elif percentage>40:
    grade="D"
else:
    grade= "F"
print("Grade: ",grade)