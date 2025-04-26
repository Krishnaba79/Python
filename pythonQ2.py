for x in range (1,11):
    print(x)

num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
if(num1>num2):
    print(num1,"is greater than",num2)
else:
    print(num2,"is greater than",num1)

num1=int(input("enter the num1:"))
num2=int(input("enter the num2:"))
print("sum is",num1+num2)

str=input("enter a number")
for x in range(len(str)-1,-1,-1):
    print(str[x])