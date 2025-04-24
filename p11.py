a = input("Enter the String:")
print(len(a))
if(len(a)<10):
    print("Invalid str must be greater than 10")
else:
    print(a[-3:-1])

a = input("Enter the String:")
print("Length of given string is:", len(a))
for i in range(len(a)-1, -1, -1):
    print(a[i])

a=input("Enter the String:")
print(a[0].upper()+a[1:])