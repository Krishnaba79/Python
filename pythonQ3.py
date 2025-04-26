a=input("enter a string:")                      #1
b=input("enter a string you want a replace:")
c=input("enter a new string:")
if(b in a):
    print(a.replace(b,c))
else:
    print("invalid")    

a=int("enter the string")                        #2
no_of_words=0
no_of_sentences=0

for i in a:
    if(i==" "):
        no_of_words+=1

        if(i=="."):
            no_of_sentence+=1

print("total no of words:",no_of_words+1)
print("total no of sentences:",no_of_sentences+1)            

a=int(input("enter the no:"))                            #3
reverse_no=0
while a!=0:
    digit=a%d
    reverse_no=reverse_no*10+digit
    a//=10
    print("reverse word is:",reverse_no)