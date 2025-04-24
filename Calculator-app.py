def add():
        print("You have selected Addition")   
        answer=b+c  
        print("Answer: ",answer)
def sub():
        print("You have selected Substraction")
        answer=b-c
        print("Answer: ",answer)
def mul():
        print("You have selected Multiplication")
        answer=b*c
        print("Answer: ",answer)

def div():
    print("You have selected Division")
    answer=int(b/c)
    print("Answer: ",answer) 
a= int(input("""Please select a option : 
1. Addition
2. Substraction
3. Multiplication
4. Division
Enter your choice:  """))
if a<=4:   
    b=int(input("type value 1 : "))
    c=int(input("type value 2 : "))
    if(a == 1):
        add()
    elif(a == 2):
        sub()
    elif(a == 3):
        mul()
    else:
        div()  
else:
    print("Your Choice: ",a)
    print("Invalid option please try again.")