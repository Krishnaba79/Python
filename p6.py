num=int(input("Enter the num:"))
for i in range(num):
    print(i)

i=1
while i<6:
    print(i)
    if(i==3):
        break
    i+=1

i=0
while i<6:
    i+=1
    if(i==3):
        continue
    print(i)

for i in range(6):
    print(i)

print(type(10))
print(type(10.67))
print(type(10j))

#print(10-4*2)

x=10
y=50
if(x ** 2 >100 and y<100):
    print(x,y)
else:
    print("Non")