def printHello():
    print("This is a Function")
printHello()

def add():
    no1=10
    no2=20
    print("Sum is:",no1+no2)
add()

def greeting():
    print("Hello,Hiral")

greeting()
greeting()

def sum():
    a=int(input("Enter the no1:"))
    b=int(input("Enter the no2:"))
    print("sum is:",a+b)
sum()

def sum():
    a=int(input("Enter the no1:"))
    b=int(input("Enter the no2:"))
    print("sum is:",a+b)

def sub():
    a=int(input("Enter the no1:"))
    b=int(input("Enter the no2:"))
    print("sub is:",a-b)

def mul():
    a=int(input("Enter the no1:"))
    b=int(input("Enter the no2:"))
    print("mul is:",a*b)

def div():
    a=int(input("Enter the no1:"))
    b=int(input("Enter the no2:"))
    print("div is:",a/b)

choice=(input("Enter the choice:"))
if(choice == 1):
    sum()
elif(choice == 2):
    sub()
elif(choice == 3):
    mul()
else:
    div()
