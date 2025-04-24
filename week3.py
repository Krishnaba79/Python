#question 1

a=int(input("Enter the No:"))
reverse_no=0
while a!=0:
    digit=a%10
    reverse_no=reverse_no*10+digit
    a//=10
print("Reverse no is:",reverse_no)

#question 4
a=input("Enter the String:")
no_of_words=0
no_of_sentences=0


for i in a:
    if(i==" "):
        no_of_words+=1

    if (i=="."):
        no_of_sentences+=1

print("Total no of words:",no_of_words+1)
print("Total no of sentence:",no_of_sentences+1)

#question 2

a=input("Enter the String:")
for i in range(0,len(a),2):
    print(a[i])

#question 3
a=input("Enter the String:")
i=0
while(i<len(a)):
    print(a[i])
    print("#")
    i+=1