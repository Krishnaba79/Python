fruits = ['banana','apple','watermelon','grapes']
for i in fruits:
    print(i)

#range: it is used to generate a sequence of numbers
for i in range(1,8):
    print(i)

for i in range(1,8,2):   # skip number like odd - even
    print(i)  

#for loops with else:
for i in range(10):
    print(i)
else:
    print("this loop is complete")    

# # break statement : use to exit the program
for i in range(10):
    print(i)
    if i==5:
        break
else :
     print("continue")   

# # continue statement: 
for i in range(10):
    
    if i==5:
        continue
    print(i)
num = int(input("enter your number:"))
for num in i:
    if (i%2==0):
     print("the value is even")
    else:
     print("the value is odd")    



    



#pass statement :  use to do nothing in program
i=4
if i>0:
    pass
print("nothing")

