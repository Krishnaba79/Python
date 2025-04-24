# ro_no=1234
# ph_no=1234567890
# txt="My roll no. is:{}, and my phone no. is:{}"
# print(txt.format(ro_no,ph_no))


# a=len("My name is Meet".split())
# print("no of words: ", a)

# b="This is the first sentence. this is the second sentence."
# c=b.count(" ")+1
# print("No. of words are: "+str(c))
# d="This is the first sentence. this is the second sentence."
# e=d.count(".")
# print("No. of sentences are: "+str(e))
# f="This is the first sentence. this is the second sentence."
# print("Total characters: ",len(f))

# a="Meezan"
# b=len(a)
# i=0
# while i<b:
#     print(a[i])
#     print("#")
#     i+=1

#Practice que-4

# string="Hello this is a simple sentence"
# a=string.count("e")
# print(a)

# string="Hello this is a simple sentence"
# count=0
# for i in string:
#     if i=='e':
#         count+=1
# print("Count of e: ",count)

# num=1
# for x in range(1,5):
#     for y in range(1,x+1):
#         print(str(num)+" ",end="")
#         num+=1
#     print()
       
# for x in range(97,102):
#     for y in range(97,x+1):
#         print(chr(x),end=" ")
#     print()
# 1)
# a=str(int(input("Enter a number")))
# b=len(a)
# for i in range(-1,-b-1,-1):
#     print(a[i])

# print(a[0::-1])
# 2)
# a="this is text"
# b=len(a)
# for i in range(0,b,2):
#     print(a[i])
# 3)
# a="Meezan"
# b=len(a)
# i=0
# while i<b:
#     print(a[i])
#     print("#")
#     i+=1
# 4)

# a=len("My name is Meet".split())
# print("no of words: ", a)

# b="This is the first sentence. this is the second sentence."
# print("Total characters:",len(b))
# c=b.count(" ")+1
# print("No. of words are:",(c))
# c=b.count(".")
# print("No. of sentences are:",c)

str="Tis a sentence1.tis sentence 2."
words=0
sentence=0
for i in str:
    if i==" ":
        words+=1
        
    if( i=="."):
        sentence+=1
        
print("total no. of words:",words+1)
print("total no. of sentence:",sentence)
# count=1
# for x in range(4):
#     for y in range(3):
#         print(count,end=" ")
#         count+=1
#         if count>=11:
#             break
#     print()

# count=0
# a="Hello this is simple sentence"
# b=input("enter a character you want to find: ")
# for i in a:
#     if i == b:
#         count+=1
# print("character",b,"was found",count,"times")


num=1
for x in range(1,5):
    for y in range(1,x+1):
        print(num,end=" ")
        num+=1
    print()
    
# for x in range(5):
#     for y in range(x):
#         print(x,end=" ")
#     print()

for x in range(1,6):
    for y in range(1,x+1):
        print(y,end=" ")
    print()

for x in range(65,70):
    for y in range(65,x+1):
        print(chr(x),end=" ")
    print()