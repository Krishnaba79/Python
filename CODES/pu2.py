    #  keyword args

# def myfunc(name):
#     print("The second no of name : " +name[1])      # print letter in same row
#     return name[1]

# letter = myfunc(name="Princy") 
# print(letter)         # print letter in second row


    #  lists and tuples

mylist=[1,2,3,3,1,5,6]

# mylist.sort()           # print number in incresing  EX : - 1,2,3,..
# print(mylist)

# mylist.pop(2)           # cut list number and than print ans
# mylist.pop(4)
# print(mylist)


    # sets 

set = {"jhon","mike","shelly"}
# print(set)

# set.add("tom")          # to add name in set
# print(set)

# set.remove("mike")          # to remove name in set
# print(set)

# set.remove("shelly")            # for upadet set
# set.add("sansa")
# print(set)

# name={"shelly","tom","mike"}                   # To updateset through function
# def updateset(set,value,newvalue):
#     set.remove(value)
#     set.add(newvalue)
# updateset (name,"shelly","sansa")
# print(name)


    # OOPS
# class Student:
#     name = "abc"
#     age = 20

# s1 = Student()
# s1.name = "rahul"
# s1.age = 12

# s2 = Student()
# s3 = Student()
# print(s1.name,s1.age)


    # constructor

# class Student:
#     def __init__(self,name,age):
#         self.StudentName = name
#         self.StudentAge = age

#     # method

#     def Say(self):
#         print("{} is {} years old".format(self.StudentName,self.StudentAge))

# s1 = Student("ABC",22)
# s2 = Student("PQR",20)

# print(s1.StudentName)
# print(s2.StudentName)

# s1.Say()
# s2.Say()


# class car:
#     def __init__(self,CarName,CarModel,CarColor): 
        

class Person:
    def __init__(self,fname,lname):
        self.firstname = fname + "Person"
        self.lastname = lname + "Person"
        print("This is person class")

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("mike ","shelly ")
print(x.firstname)