
#class

"""class Person():
    name="Hiral"
    age="18"
    location="Ahmedabad"


    def speak(self):
        print("Hello from speak")

    def walk(self):
        print("Hello from walk")

p1=Person()
print(p1.name)
print(p1.age)
print(p1.location)

p2=Person()
p2.name="abc"
print(p2.name)
print(p2.age)
print(p2.location)

p1.speak()
p1.walk()

class Book1():
    name="ABC"
    author="Author1"
    year="2010"
    chapters="5"

    def hello(self):
        print("Hello")

b1=Book1()
print(b1.name)
print(b1.author)
print(b1.year)
print(b1.chapters)

b1.hello()

b2=Book1()
b2.name="XYZ"
print(b2.name)
b2.author="Author2"
print(b2.author)
b2.year="2014"
print(b2.year)
b2.chapters="2"
print(b2.chapters)

b2.hello()

b3=Book1()
b3.name="PQR"
print(b3.name)
b3.author="Author3"
print(b3.author)
b3.year="2008"
print(b3.year)
b3.chapters="7"
print(b3.chapters)

b3.hello()

programing=[b1,b2]
general=[b3]"""


class Book():
    name=""
    year=""
    author=""
    chapter=""


    def __init__(self,pname,pyear,pauthor,pchappters):
        #print(pname)
        #print(pyear)
        #print(pauthor)
        #print(pchappters)

        self.name=pname
        self.year=pyear
        self.author=pauthor
        self.chapter=pchappters



b1=Book("ABC",2010,"PQR",5)
print(b1.name)








