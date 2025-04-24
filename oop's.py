''' types of function: 1. instance function: def__int__(self,a,b), selfname.a,self.color.b,c1=car("abc",black")
in instance func. must be added self'''



class person():
    def __init__(self,fname,lname,roll):
        self.firstname=fname
        self.lastname=lname
        self.roll=roll
    def printhello(self):
        print("hello", self.firstname)
class student(person):
    pass


s1=student("lija","abc",32)
s1.printhello()
