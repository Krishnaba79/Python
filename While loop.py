# i = 0
# while ( i < 10):
#     i+=1
#     if ( i == 4 ):
#         continue
#     print(i)

str=input("Enter string: ")
index=int(input("Enter index: "))
count=-1
while count<len(str)-1:
    count+=1
    if index==count:
        continue
    else:
        print(str[count])       