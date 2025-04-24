#    765432109876543210 -
a= ("Python Programming")
#    012345678901234567 +
for i in a :
    print (i)
'''Positive string slicing'''
print(a.capitalize())
print(a.casefold())
print(a.center(75,"*"))
print(a.endswith("ng"))
print(a.find("Prog"))
print(a.index("P"))
print(a.isalnum()) #isalnum=is alphabet + numeric
print("Meet".isalpha())
print(a.upper())
print(a.lower())
print(a.replace("m","w"))
print(a.swapcase())
print("Python programming classes".title())
print("m" in a)
print(a[1:10])
print(a[:15])
print(a[5:])
print(a[1:16:2])
print(a[: :3])
'''Negative string slicing'''
print(a[-17:-1])
print(a[:-5])
print(a[-15:])
print(a[-14:-1:2])
print(a[::-1])