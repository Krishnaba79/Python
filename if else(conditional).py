'''if(condition1):            # if condition 1 is true
    print("yes")
elif(condition2):             # if condition 2 is true
    print("no") 
else:                         #otherwise
    print("maybe")'''

# 1 if-elif-else ladder in python
a=17
if(a<3):
    print("the value of a is greater than 3")
elif(a>7):
    print("the value of a is greater than 7")
else:
    print("the value is not greater than 3 or 7") 

# 2 multiple if statements
a=10
if(a>3):
    print("the value of a is greater than 3")
if(a>7):
    print("the value of a is greater than 7")
if(a>17):    
    print("the value of a is greater than 17")
else:
    print("the value is not greater than 3 or 7") 

a=22
if(a>9):
    print("greater")
else:
    print("lesser")

age = int(input("enter your age:"))
if(age>18):
    print("yes")
else:
    print("no")    


''' there can be any number of elif statements,
    last else is executed only if all the conditions inside elifs fail'''
