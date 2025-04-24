
a=input("Enter roll no:")
b=input("Enter phone no:")
txt=("My roll no is {} and my phone no is {}")
print(txt.format(a,b))

digit=10
txt="I have ten apples ten ten ten"
txt=txt.replace("ten","{}")
print(txt)
print(txt.format(digit,10,20,30))

str="{} * {} = {}"
for i in range(1,11):
    print(str.format(2,i,2*i))
