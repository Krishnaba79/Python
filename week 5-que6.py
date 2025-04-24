#week 5-que6
# a=int(input("""Select an option
# 1)Convert Dollar to INR
# 2)Convert INR to Dollar

# Enter Your choice: """))
# Dollar=82.75
# if a<=2:
#     if a==1:
#         b=int(input("Enter Dollar amount: "))
#         c="INR: {} Rs"
#         print(c.format(b*Dollar))
#     else:
#         b=int(input("Enter INR amount: "))
#         c="Dollar: {} $"
#         print(c.format(b/Dollar))
# else:
#     print("Invalid choice")

#Que 1

# nme=input("Enter Student name: ")
# sub1=int(input("Enter marks in sub 1: "))
# sub2=int(input("Enter marks in sub 2: "))    
# sub3=int(input("Enter marks in sub 3: "))
# per=(sub1+sub2+sub3)/3
# if per>=80:
#     grade="A"
# elif per>60:
#     grade="B"
# elif per>40:
#     grade="C"
# else:
#     grade="D"
# a=(nme+" got {} % and grade {}")
# print(a.format(per,grade))

#factorial
# n=int(input("enter a number: "))
# fact=1
# for i in range(1,n+1):
#     fact*=i
# print(fact)

#bin2dec
# bin=(input("Enter a num: "))
# dec=0
# for i in bin:
#     if int(bin) or i==8:
#         dec=dec*2 +int(i)
# print(dec)

#pattern

for rows in range(1,6):
    for space in range(1,6-rows):
        print(" ",end="")
    for cols in range(rows):
        print("#",end="")
    if (rows in {1,2,3,4,5}):
        print(" ", end=" ")
    for cols in range(rows):
        print("#",end="")
    print()
#2
for x in range(0,6):
    print(" "*(6-x)," *"*x)
for x in range(6,0,-1):
    print(" "*(6-x)," *"*x)