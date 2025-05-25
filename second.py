#type conversion :
old_age= input("Enter your old age:")
new_age = int(old_age) + 2
print(new_age)

# type conversion in float:
number = 18
print(float(18))

# print sum of 2 numbers:
first = input("enter first number:")
second = input("enter second number:")
sum=int(first)+int(second)
print("the sum is :" + str(sum))

# Strings:
name = "Tony Stark"
print(name.upper())
print(name)
print(name.lower())
print(name.find('S'))
print(name.find('s'))
print(name.find('Stark'))
print(name.find('stark'))
print(name.replace("Tony Stark","Ironman"))
print(name)
print(name.replace("Stark","Ironman"))
print(name.replace("T","M"))

# Keywords:
print('T' in name) # output: True
print('m' in name) # output: False
print("Stark" in name)
print("Ironman" in name) # output: False

# Arithmetic Operator :
print(5+2)
print(5-2)
print(5*2)
print(5/2) # output = 2.5
print(5 // 2) # output = 2
print(5%2) # output = 1
print(5 ** 2) # output = 25 

#Shortcuts :
# i= 5
# i = i+2  
# i += 2
# i -= 2
# i *= 2

# Operator Precedence :
result = (2 + 3) * 5
print(result)
result1 = 2 + 3 * 5
result2= 2+3/5

#comments :
# here is a comment
# taking input
#calculate sum

# Comparsion Operators :
print(3>2) # output True
print(3<2) 
print(3<=2)
print(3>=2)
print(3==3)
print(3==2)
print(3 != 3)
print(3!=2)

# Logical Operators :
print( 2>3 or 2>1)
print(3>2 and 2>1)
print(3>2 and 2>6)
print(not 2>3)
print(not 3>2)

# if - else Statements :
#age = 19
#age = 13
#age=2
age = 16
if age >= 18:
    print("you are an adult")
    print("you can vote")
elif age < 18 and age>3:
    print("you are in school")
else:
    print("you are a child")
print("Thnak you")

# Excercise:
first = input("enter first number:")
operator=input("enter operator(+,-,*,/,%) :")
second = input("enter second number:")
first=int(first)
second=int(second)
if operator == "+" :
    print("first+second")
elif operator == "-" :
    print("first-second")
elif operator == "*" :
    print("first*second")
elif operator == "/" :
    print("first/second")
elif operator == "%" :
    print("first % second")
else:
    print("Invalid Operator")

# Range :
numbers = range(5) # 0,1,2,3,4
print(numbers)
 
# While Loops :
i = 1
while i <= 10000: #100 #5
    print(i)
    i = i +1
k=1  #5
while k<=5: #<=0
    print(k * "*") #hello
    i=i+1 #-1

# for Loops :
for item in range(5):
    print(item+1)

# List :
marks = [95,98,97]
print(marks[0]) #[1]
print(marks[-1]) #outpput 97
print(marks[0:2])
print(marks[1:3])

#for loop in lists :
marks1=[95,98,97]
for score in marks1:
    print(score)
marks.append(99)
print(marks)
marks.insert(0,99)
print(marks)
print(99 in marks)
print(93 in marks)
print(len(marks))
i=0
while i < len(marks):
    print(marks[i])
    i = i +1
marks.clear()
print(marks)

# Break & Continue :
students=["ram","shyam","kishan","radha","radhika"]
for student in students:
    if student ==  "radha":
        break;
    print(student)
for student in students:
    if student == "kishan":
        continue;
    print(student)

# Tuple :
marks=(95,98,97,97,97)
print(marks.count(97))
print(marks.count(95))
print(marks.index(97))

# Set :
marks={95,98,97,97,97}
person="ram","shyam","abhi"
print(person)
print(marks)
# print(marks[0])  output :error
for score in marks:
    print(score)

# Dictionary :
marks={"english":95,"chemistry":98}
information = {"ram":"nalkishan"}
print(marks["chemistry"])
marks["physics"] = 97;
print(marks)
marks["physics"] = 99;
print(marks)

# Functions :
# 1. In-built Functions
int()
str()
bool()
# 2 . Moddule Functions
import math
print(dir(math))
from math import sqrt
print(sqrt(4))
print(sqrt(16))
from math import *
# 3 . User Define Functions
# syntax : 
# def function_name(parameters):
    # do something
def print_sum(first,second=4): #(first,second)
    print(first+second)
print_sum(1) # print(1,2)