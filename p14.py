'''for i in range(5):
    for j in range(i):
        print("*", end="")
    print("")

for i in range(5):
    for j in range(4-i+1):
        print("*", end="")
    print("")

for i in range(5):
    for k in range(4-i):
        print(" ", end="")

    for j in range(i+1):
        print("*", end=" ")
    print("")

for i in range(5):
    for k in range(i):
        print(" ", end="")
    for j in range(5-i):
        print("*", end=" ")
    print()

for i in range(5):
    for k in range(i):
        print(" ", end="")
    for j in range(5-i):
        print("*", end="")
    print()'''

'''for i in range(5):
    for k in range(5-i):
        print(" ", end="")
    for j in range(i+1):
        print("*", end=" ")
    print()
for i in range(5):
    for k in range(i+1):
        print(" ", end="")
    for j in range(5-i):
        print("*", end=" ")
    print()'''

count=1
for i in range(4):
    for j in range(3):
        print(count,end="")
        count +=1
        if(count>10):
            break
    print()

for i in range(6):
    for j in range(i):
        print(j,end="")
    print()

b=0
for i in range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(i,end="")
    print()

for i in range(1,5+1):
    for j in range(1,i+1):
        print(j,end="")
    print()


for i in range(5,0,-1):
    for j in range(0,i):
        print(5,end="")
    print()


for i in range(1,6):
    for j in  range(i,0,-1):
        print(j,end="")
    print()


for i in range(5,0,-1):
    for j in range(0,i+1):
        print(j,end="")
    print()

no=1
stop=2
for i in range(3):
    for j in range(1,stop):
        print(no,end="")
        no+=1
    print()
    stop+=2