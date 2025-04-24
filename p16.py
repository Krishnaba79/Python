def IsValidIndex(i,len):
    if(i>=0) and (i<len):
        return True
    else:
        return False

mylist=[1,2,3,4,5]
print(mylist)
index=int(input("Enter an index no:"))
result=IsValidIndex(index,len(mylist))

if result:
    print("Valid Index")
    mylist[index]=int(input("Enter the new value:"))
    print(mylist)
else:
    print("Invalid index")
