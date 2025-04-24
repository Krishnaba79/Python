a=input("Enter the student name:")
sub1=int(input("Enter the marks of Sub1:"))
sub2=int(input("Enter the marks of Sub2:"))
sub3=int(input("Enter the marks of Sub3:"))
sub4=int(input("Enter the marks of Sub4:"))
total=sub1+sub2+sub3+sub4
print(total)
pr=total/400*100
print(pr)

while True:
    if(pr>=80) and (pr<=100):
        print("Grade A")
        break
    elif(pr>=60) and (pr<=79):
        print("Grade B")
        break
    elif(pr>40) and (pr<59):
        print("Grade C")
        break
    else:
        print("Grade D")
        break

print(a,"got",pr,"% and",)


