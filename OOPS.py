''' Object Oriented Programming
Anything that stores data on hard disk is called object
For eg: Variables, List,every data type,etc
We can create our own data type'''

'''OBJECTS
     variables are attribute/property
     Functions are behaviours/methods
CLASS
    Is a blueprint'''


# class car():
#     def start(self):
#         print("Hello")
# car1=car()
# print(type(car1))
# car1.start()

# class person():
#     age =10
#     height=150
#     def speak(self):
#         print("This is speak function")
# meet=person()
# b=meet.speak()
# print(meet.height)
# print(meet.age)

# class book():
#     name="Lightning thief"
#     author="Rick Riordan"
#     year= 2010
#     chapters=12
#     def hello(self):
#         print("Hello")
        
# a=book()
# print(a.name,a.author,a.year,a.chapters,sep=("\n"))

# book1=book
# book1.name="House of Hades"
# book1.author="Rick Jorddan"
# book1.year=2012
# book1.chapters=24
# print(book1.name,book1.author,book1.year,book1.chapters,sep=("\n"))
# book2=book
# book2.name="Magnus Chase"
# book2.author="Rick Jorddan"
# book2.year=2020
# book2.chapters=56
# print(book2.name,book2.author,book2.year,book2.chapters,sep=("\n"))
# book3=book
# book3.name="Trials of Apollo"
# book3.author="Rick Jorddan"
# book3.year=2016
# book3.chapters=64
# print(book3.name,book3.author,book3.year,book3.chapters,sep=("\n"))

# class book():
#     name=""
#     author=""
#     year=""
#     chapters=""
#     def __init__(self,name,author,year,chap):
#         self.name=name
#         self.author=author
#         self.year=year
#         self.chapters=chap
# b1=book("Percy Jackson","Rick",2012,[1,2,3,4,5])
# print(book1.name,book1.author,book1.year,book1.chapters,sep=("\n"))

# b2=book("Magnus Chase","Rick Riordan",2020,[1,2,3,4,5,6,7,8,9,10])
# print(book2.name,book2.author,book2.year,book2.chapters,sep=("\n"))

#================================


# class book():
#     def __init__(self,name,author,year,chap,cate):
#         self.name=name
#         self.author=author
#         self.year=year
#         self.chapters=chap
#         self.categories=cate
# b1=book("book1","Meet",2012,56,"SELF")
# b2=book("book2","Meet. H",2016,32,"NEW")
# b3=book("book3","Meet Vasani",2020,69,"NEW")
# abc=[]
# SELF=[]
# if "SELF" in b1.categories:
#      SELF.append(b1)
# else:
#     abc.append(b1)
# if "SELF" in b2.categories:
#      SELF.append(b2)
# else:
#     abc.append(b2)
# if "SELF" in b3.categories:
#      SELF.append(b3)
# else:
#     abc.append(b3)
# # print("NEW: ",NEW)
# # print("SELF: ",SELF)
# b=len(abc)
# # c=len(SELF)
# for i in abc:
#     print(i.name)

# class car():
#     def fuel(self):
#         print("Fuel")
#     def ride(self):
#         print("Ride")
    
#     def __init__(self,name,speed,color,model):
#         self.name=name
#         self.speed=speed
#         self.color=color
#         self.model=model
# c1=car("Mercedes",250,"Red","G360")
# c2=car("Kia",120,"Blue","Seltos")
# c3=car("Supra",200,"Red","Sports")
# c4=car("Mustang",190,"Blue","GT")
# cars=[c1,c2,c3,c4]
# for i in cars:
#     print(i.name)


#TYPES OF FUNC.
#1) Instance
#2) Class
#3) Static 



# class Car():
#     wheels=4
#     def __init__(self,a,b) :
#         self.name=a
#         self.color=b
#     def getName(self):
#         print(self.name)
#     def getcolor(self):
#         print(self.color)
#     def getall(self):
#         print(self.name)
#         print(self.color)
#     def setname(self,p):
#         self.name=p
        
#     def getwheels(cls):
#         print(cls.wheels)
#     @classmethod
#     def setwheels(cls,wheel):
#         cls.wheels=wheel
    
# c1=Car("ABC","Black")
# c2=Car("XYZ","Yellow")
# c1.setname("DEF")
# c1.getall()
# c1.getwheels()
# Car.setwheels(5)
# c2.getwheels()
'''INHERITANCE
    Inheriting one data type in another'''
# class Person():
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def getall(self):
#         print(self.fname,self.lname)
#         print()

# class student(Person): #inheriting class Person
#     pass
# s1=student("Meet","Vasani")
# s1.getall()

# class Person():
   
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#     def getall(self):
#         print(self.fname,self.lname)
# class Student(Person):
#     pass

# a=input("Enter first name: ")
# b=input("Enter last name: ")
# a=Student(a,b)
# a.getall()

'''ABSTRACTION
    Details are hidden'''
    
'''ENCAPSULATION
    Packing many data types as one(using our own data type)'''

'''SCOPE
    Scope is where is variable declared
    varibles out of class is global scope and variables inside it is called local scope
    variables inside class can be converted by writing("abc")'''
# class me():
#     global b
#     b=20
#     # print(b)
# # me()
# print(b)

"""MODULES
Importing file to another programme"""
# import Pattern
# a=Pattern
# print(a)