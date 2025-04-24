"""Sequential Data Types/Collection Data Types
# 4 Types"""
"""We can create a list using []
for eg:- MyList=[1,'name',0.24,true] """
'''Ordered list:
    >Items have defined order, and that order won't change.
    >INDEXING is used. 
    >It is changable. : Mylist[0]=22 
    >Duplications allowed '''

# def isvalidindex(index,len):
#     if index>=0 and index<len:
#         return True
#     else:
#         return False
# Mylist=[10,20,30,40,50]
# index=int(input("Enter index: "))
# result=isvalidindex(index,len(Mylist))
# if result:
#     print("Valid Index")
#     newvalue=int(input("enter a new value: "))
#     Mylist [index] = newvalue
#     print(Mylist)
# else:
#     print('invalid index')

#create a list of your friends name and print it
# a=['hetvi','ishwa','roshan','koyna','jainil']
# for i in range(len(a)):
#     print(a[i])
# print()
# b=[1,2,3,4,5,6,7,8,9,10]
# for x in range(len(b)):
#     print(b[x])
# print()
# for i in b:
#     if i%2!=0:
#         print(b[i])
# print()

# ph_no=[1020101001,1210101010,1324567890]
# count=0
# for i in ph_no:
#     print(str(i)[1])
# print()
mylist=[]
odd=[]
even=[]
for i in range (5):
    a=int(input("enter a number: "))
    mylist.append(a)
print()
for x in mylist:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)

    # if a%2==0:
    #     even.append(a)
    # else:
    #     odd.append(a)
print('Mylist: ',mylist)
print('Odd',odd)
print('Even: ',even)