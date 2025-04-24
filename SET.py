#SET:- {}
# x index
# x changes
# x duplicatons

# set1= {1,2,3,2,4,"Meet",3}
# set1.add(10) #append func
# print ((set1))
# set2={5,6,7,8,9,10,"Roshan"}
# set1.update(set2) #extend func
# print(set1)

# for i in set1:
#     print(i)
# set1.remove("Meet")
# print(set1)
# set1.discard("Roshan")
# print(set1)
# set1.pop()
# print(set1)
# set1.clear()
# print(set1)

# c=set1.union(set2) # Union of sets
# print(c)

# print(set1.union(set2))
# a=10
# print(id(a),a) #for address of a on hardisk in decimal
# b=a
# b=a+2
# print(id(b),b)
# print(a is b)
# d={"Meet@","Roshan@"}
# print(d)
# list=[(1,2,3),(4,5,6)]
# print(list)

# emailid=[]
# valid=[]
# nonvalid=[]
# for i in range(5):
#     a=input("Enter gmail:")
#     emailid.append(a)
#     if a.endswith("@gmail.com"):
#         valid.append(a)
#     else:
#         nonvalid.append(a)
# print("ID you entered: ",emailid)
# print("Valid ID: ",valid)
# print("Non-valid ID: ",nonvalid)

# @gmail.com- len:10

# emailid=[]
# valid=[]
# nonvalid=[]
# for i in range(5):
#     a=input("Enter gmail:")
#     emailid.append(a)
#     if a[-10:]=="@gmail.com":
#         valid.append(a)
#     else:
#         nonvalid.append(a)
# print("ID you entered: ",emailid)
# print("Valid ID: ",valid)
# print("Non-valid ID: ",nonvalid)


# a="The quick Brow Fox"
# countupper=0
# countlower=0
# for i in a:
#     if i.islower() and i!=" ":
#         countlower+=1
#     elif i==" ":
#         pass
#     else:
#         countupper+=1
# print()
# print(countupper)
# print(countlower)

# s1={1,2,3,3,4,7,5,6}
# s2={7,8,9,10}

# print(s1.union(s2))
# print(s2.intersection(s1))
# print(s1.symmetric_difference(s2))

# a={"a","b","c","d"}
# b={"A","B","c",1,4,"d"}

# mutuals=(a.intersection(b))
# print("Mutuals of a and b: ",mutuals)

fname=set()
lname=set()
fu_name=set()
def name():
    for i in range(3):
        full_name=input("Enter full name: ")
        fu_name.add(full_name)
        b=(full_name.index(" "))
        first_name=full_name[:b] 
        fname.add(first_name)
        lastname=full_name[b+1:]
        lname.add(lastname)
name()
print(fname)
print(lname)