print("PLease select the option")
print("        1. Addition")
print("        2. Substraction")
print("        3. Multiplication")
print("        4. Division")

while True:
    choice=input("Enter your choice:")
    if choice in ("1", "2", "3", "4"):
        if choice == '1':
            print("your choice : 1")
            print("You have selected Addition ")

        elif choice == '2':
            print("your choice : 2")
            print("You have selected Substraction")

        elif choice == '3':
            print("your choice : 3")
            print("You have selected Multiplication")

        elif chice == '4':
            print("your choice : 4")
            print("You have selected Division")

    if choice in ("1", "2", "3", "4"):
        a=int(input("Enter the value of A:"))
        b=int(input("Enter the value of B:"))

        if choice == '1':
            print("Answer :", a+b)

        elif choice == '2':
            print("Answer :", a-b)

        elif choice == '3':
            print("Answer :", a*b)

        elif choice == '4':
            print("Answer :", a/b)

    else:
        print("Invalid option")




