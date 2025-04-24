for i in range(0,11):
    print(i)
print("___________________________________")
for i in range(3,11):
    print(i)
print("___________________________________")
for i in range(10,0,-1):
    print(i)
print("___________________________________")
for i in range(0,11,2):
    print(i)
print("___________________________________")
i=int(input("Enter value of I: "))
for i in range(i,i*10+1,i):
    print(i)
print("___________________________________")
n=int(input("Enter N: "))
sum=0
for i in range(1,n+1):
    sum=sum+i
print("Sum: ",sum)
print("___________________________________")