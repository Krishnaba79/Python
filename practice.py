#q=1
mydict={
    "pankha":"fan",
    "ghadi":"watch",
    "khidki":"window"
}
a =input("enter your hindi word:\n",)
print("the meaning of your word is:",mydict[a])

#q=2
a=input("enter first number:")
b=input("enter second number:")
c=input("enter third number:")
d=input("enter fourth number:")
e=input("enter fifth number:")
f=input("enter sixth number:")
g=input("enter seventh number:")
h=input("enter eighth number:")

mydict={a,b,c,d,e,f,g,h}
print(mydict)

#q=3
set=(18,"18")
print(set)

q=4
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(s)
print(len(s))

q=5
s={}
print(type(s))

q=6,7,8
favlang={}
a=input("favourite language of shubham:\n")
b=input("favourite language of harshita:\n")
c=input("favourite language of lija:\n")
d=input("favourite language of krishna:\n")
favlang['shubham favlang is:']=a
favlang['harshita favlang is']=b
favlang['lija favlang is']=c
favlang['krishna favlang is']=d
print(favlang)

q=9
s={8,7,12,"harry",[1,2]}  
# its not valid,can't add list in dictionary so can't change value of list
                    