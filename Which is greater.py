a=int(input("Type value of A : "))
b=int(input("Type value of B : "))
c=int(input("Type value of C : "))
if a>b:
    if a>c:
        print("A is greater")
    else:
        print("C is greater")
elif b>c:
        print("B is greater")
else:
    print("C is greater")