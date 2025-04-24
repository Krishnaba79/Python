#question 1

count=1
for i in range(4):
    for j in range(3):
        print(count,end="")
        count +=1
        if(count>10):
            break
    print()

#question 2
a="Hello this is a simple sentence"
print("no of char was found:",a.upper())

#question 3
print("1", "2", "3", "4" , "5" , sep="#",end="@")
print("6", "7", "8", "9", "10", sep="#",end="@")
print("11", "12", "13", "14", "15",sep="#",end="@")

#question 4
print("\nTwinkle, twinkle,little star,\n      How are wonder what you are!\n              Up above the world so high,\n             Like a diamond in the sky.\n ""Twinkle,twinkle,little star,\n      How are wonder what you are")

#question 5

print("Ohhh! Hi, How are you? That's your book?\n Nice//\\  this is tab space;0")

#question 6
num=1
for i in range(0,4):
    for j in range(0,i+1):
        print(num,end="")
        num=num+1
    print("\r")

no=1
for i in range(0,6):
    for j in range(no,i+1):
        print(j,end="")
        i+=1
    print()

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()